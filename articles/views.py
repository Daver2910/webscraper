# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(request):
    return render('this is the homepage and /articles/ page')

def index(request):
	return HttpResponse('this is the homepage and /articles/ page')

def index1(request):
    return render(request, 'articles/base.html', {})