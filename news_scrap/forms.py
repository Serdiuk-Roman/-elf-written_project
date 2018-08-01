#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from .models import ShortNews


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = ShortNews
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
