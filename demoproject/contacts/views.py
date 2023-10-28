from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contacts(request):
    text = '<h1>This is an H1 heading</h1>'
    return HttpResponse(text)


