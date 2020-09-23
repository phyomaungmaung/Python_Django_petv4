from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# importing loading from django template
from django.template import loader

def index(request):
    template = loader.get_template('2_index_tvariable.html') # getting our template
    # context
    name = {
        'student':'kyaw kyaw'
    }
    return HttpResponse(template.render(name))
    # rendering the template in HttpResponse