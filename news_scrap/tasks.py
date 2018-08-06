
# pip install requests
# pip install beautifulsoup4

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from bs4 import BeautifulSoup
import requests

channel_layer = get_channel_layer()


@shared_task
def parser_news():

    url = "https://ua.censor.net.ua/news/all"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    main_block = soup.find(class_="curpane")
    main_list = main_block.find_all(
        'article',
        {"class": "item"},
    )
    news_el = [
        {
            "title": el.find("h3").text,
            "time": el.find("time").get("datetime"),
            "link_url": el.find("a").get("href"),
            "short_text": el.find("div", {"class": "anounce"}).find("a").text,
        }
        for el in main_list
    ]
    async_to_sync(channel_layer.group_send)(
        "news", {"type": "new.news", "text": news_el}
    )


@shared_task
def parse_post(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    short_text = soup.find("h2", {'itemprop': "description"}).text
    text = short_text + soup.find("div", {"class": "entry-content"}).get_text()
    news_el = {
        "link_url": url,
        "post_title": soup.find(class_="entry-title").text,
        "datetime": soup.find("time",
                              {"class": "published dateline"}).get("datetime"),
        "full_text": text,
    }

    async_to_sync(channel_layer.group_send)(
        "news", {"type": "new.post", "text": news_el}
    )
