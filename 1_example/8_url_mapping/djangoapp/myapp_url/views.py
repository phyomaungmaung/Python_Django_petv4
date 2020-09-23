from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Employee

@require_http_methods(["GET"])
def hello(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')

def get_employee(request, employee_id):
    List = []
    employee = Employee.objects.get(id=employee_id)
    first_name = employee.first_name
    last_name = employee.last_name
    List.append(first_name + ' ' + last_name)
    return HttpResponse(List)