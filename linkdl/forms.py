#-*- coding:utf-8 -*-
from fileinput import filename
from .models import Link
from django import forms

class LinkForm(forms.ModelForm):
    filename=forms.CharField(max_length=100)
    class Meta:
        model = Link
        fields = "__all__"
