from django.conf.urls import url, include
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
