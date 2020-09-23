from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    if True:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    else:
        return HttpResponse('<h1>Page was found</h1>') 
        # rendering the template in HttpResponse