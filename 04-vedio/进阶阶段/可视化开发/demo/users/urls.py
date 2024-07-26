"""
    @project: stuPython
    @Author：Murk
    @file： urls.py
    @date：2024/7/26 20:58
    @Desc: 
"""
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
]