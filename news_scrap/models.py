#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class ShortNews(models.Model):
    news_link = models.URLField(unique=True)
    title = models.CharField(max_length=128)
    datetime = models.DateTimeField()
    # img = models.FileField()
    full_text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
