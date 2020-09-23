from django.shortcuts import render

# Create your views here.

def index(request):
    pet_list = ['Garfy','Lucky','Casy','Princess']
    return render(request,'5_index_ttagscomment.html',{ "pet_list": pet_list })