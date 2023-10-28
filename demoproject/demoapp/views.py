from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request : HttpRequest):
    method = request.method
    scheme = request.scheme
    msg= "{0} is the request and {1} is the scheme and Hello world".format(method,scheme)
    return HttpResponse(msg)