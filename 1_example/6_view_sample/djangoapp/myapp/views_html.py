from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)
    # rendering the template in HttpResponse