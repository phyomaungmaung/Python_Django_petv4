from django.shortcuts import render

# Create your views here.

def index(request):
    pet_list = ['Garfy','Lucky','Casy','Princess']
    return render(request,'4_index_ttagsfor.html',{ "pet_list": pet_list })