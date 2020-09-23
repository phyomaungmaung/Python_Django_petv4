from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['first_name','age','contact','email']

admin.site.register(Employee,EmployeeAdmin)