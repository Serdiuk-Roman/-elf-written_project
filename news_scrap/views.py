#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import reverse_lazy
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import FormView, CreateView,\
#     UpdateView, DeleteView

# from news_scrap.models import ShortNews
# from news_scrap.forms import NewsModelForm

from .tasks import parse_post


def index(request):
    return render(request, "news_scrap/news.html", {})


def create_n(request):
    link = request.GET.get('news_url', '')
    parse_post.delay(link)
    return HttpResponse()


# class NewsListView(ListView):
#     model = ShortNews
#     template_name = 'news_scrap/list.html'

#     def get_context_data(self, **kwargs):
#         context = super(NewsListView, self).get_context_data(**kwargs)
#         context['form'] = NewsModelForm()
#         return context


# class NewsDetailView(DetailView):
#     model = ShortNews
#     template_name = 'news_scrap/detail.html'


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


# class NewsDeleteView(DeleteView):
#     model = ShortNews
#     success_url = reverse_lazy('news_list')
