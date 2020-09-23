from django.shortcuts import render, redirect

# Create your views here.
from myapp_model_form.forms import StudentForm
from myapp_model_form.models import Student

def index_html(request):
    student = Student()
    return render(request,"1_index_html.html",{'student':student})

def save_html(request):
    if request.method == "POST": 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student = Student.objects.create(first_name=first_name,last_name=last_name)
        student.save()
        return redirect('/index_html')
    else:
        student = Student()
    return render(request,"1_index_html.html",{'student': student})

def index_form(request):
    form = StudentForm()
    return render(request,"2_index_form.html",{'form':form})

def save_form(request):
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():   
            form.save()
            return redirect('/index_form')
    else:
        form = StudentForm()
    return render(request,"2_index_form.html",{'form': form})
    