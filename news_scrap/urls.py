#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from news_scrap.views import index, create_news
from news_scrap.views import NewsListView, NewsDetailView, NewsDeleteView
# NewsFormView, NewsCreateView, NewsUpdateView,

urlpatterns = [
    path('',
         index,
         name="index"),
    path(
        'create/',
        create_news,
    ),

    url(
        r'(?P<pk>[0-9a-f\-]+)$',
        NewsDetailView.as_view(),
        name="news_detail"
    ),
    url(
        r'(?P<pk>[0-9a-f\-]+)/delete/$',
        NewsDeleteView.as_view(),
        name="news_delete"
    ),
    path(
        'news/',
        NewsListView.as_view(),
        name="news_list"
    ),

    # url(
    #     r'add/$',
    #     NewsFormView.as_view(),
    #     name="news_form"
    # ),
    # path(
    #     'create/',
    #     NewsCreateView.as_view(),
    #     name="news_create"
    # ),
    # url(
    #     r'(?P<pk>[0-9a-f\-]+)/udate/$',
    #     NewsUpdateView.as_view(),
    #     name="news_update"
    # ),

]
