from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .tasks import parser_news


class NewsConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "news", self.channel_name
        )
        self.accept()
        parser_news.delay()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "news", self.channel_name
        )

    def new_news(self, event):
        message = json.dumps({
            "news_list": event["text"],
            "type": "list"
        })
        self.send(text_data=message)

    def new_post(self, event):
        message = json.dumps({
            "best_post": event["text"],
            "type": "single"
        })
        self.send(text_data=message)
