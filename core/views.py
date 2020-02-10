# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request, *args, **kwargs):
    return render(request, 'index.html')

def contact(request, *args, **kwargs):
    return render(request, 'contact.html')