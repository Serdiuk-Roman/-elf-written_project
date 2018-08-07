#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
# FormView, CreateView, UpdateView

# from news_scrap.forms import NewsModelForm

from .tasks import parse_post
from .models import ShortNews

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


def index(request):
    return render(request, "news_scrap/news.html", {})


def create_news(request):
    link = request.GET.get('news_url', '')
    try:
        db_post = ShortNews.objects.get(news_link=link)
        news_el = {
            "news_link": db_post.news_link,
            "post_title": db_post.post_title,
            "post_datetime": json.dumps(db_post.post_datetime.isoformat()),
            "full_text": db_post.full_text,
        }
        async_to_sync(channel_layer.group_send)(
            "news", {"type": "new.post", "text": news_el}
        )
    except ShortNews.DoesNotExist:
        parse_post.delay(link)
    return HttpResponse()


class NewsListView(ListView):
    model = ShortNews
    template_name = 'news_scrap/list.html'
    ordering = ['-pk']

    # def get_queryset(self):
    #     qs = ShortNews.objects.order_by('-pk')
    #     return qs


class NewsDetailView(DetailView):
    model = ShortNews
    template_name = 'news_scrap/detail.html'


class NewsDeleteView(DeleteView):
    model = ShortNews
    success_url = reverse_lazy('news_list')


# class NewsFormView(FormView):
#     form_class = NewsModelForm
#     template_name = 'news_scrap/form.html'
#     success_url = '/'


# class NewsCreateView(CreateView):
#     model = ShortNews
#     template_name = 'news_scrap/create.html'
#     fields = '__all__'


# class NewsUpdateView(UpdateView):
#     model = ShortNews
#     fields = '__all__'
#     template_name_suffix = '_update_form'
