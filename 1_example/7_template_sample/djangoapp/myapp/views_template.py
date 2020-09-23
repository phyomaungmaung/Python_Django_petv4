from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# importing loading from django template
from django.template import loader

def index(request):
    template = loader.get_template('1_index_template.html') # getting our template
    return HttpResponse(template.render())
    # rendering the template in HttpResponse