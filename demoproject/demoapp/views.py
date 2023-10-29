from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request : HttpRequest, name , id ):
    method = request.method
    scheme = request.scheme
    msg= "{0} is the request and {1} is the scheme and Hello world. And the name is {2} with the id {3}".format(method,scheme,name,id)
    return HttpResponse(msg)


def qrv (request : HttpRequest):
    name = request.GET['name']
    id = request.GET['id']
    method = request.method
    scheme = request.scheme
    msg= "{0} is the request and {1} is the scheme and Hello world. And the name is {2} with the id {3}".format(method,scheme,name,id)
    return HttpResponse(msg)