#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class ShortNews(models.Model):
    news_link = models.URLField()
    title = models.CharField(max_length=128)
    # img = models.FileField()
    lid = models.TextField()
    author = models.CharField(max_length=64)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
