from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp_form.forms import StudentForm

def index(request):
    student = StudentForm()
    return render(request,"index.html",{'form':student})