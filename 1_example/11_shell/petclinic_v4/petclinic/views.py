from django.shortcuts import render
from .models import Owner

# Create your views here.
def all_owners(request):
    owners_list = Owner.objects.all()
    return render(request,'owners.html', {'owners_list': owners_list})