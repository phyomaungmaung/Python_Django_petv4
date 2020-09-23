from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'3_index_ttagsif.html')
    # rendering the template in HttpResponse