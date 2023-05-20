from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def amma(request):
    return HttpResponse('<marquee><h1>i love you maaa</h1></marquee>')

def bujji(request):
    return HttpResponse('<marquee><h1>she looking so beautiful</h1></marquee>')
