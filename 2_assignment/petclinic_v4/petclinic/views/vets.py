from django.shortcuts import render
from ..models import Vet

# Create your views here.

def all_vets(request):
    all_vets = Vet.objects.all()
    context = { "all_vets": all_vets }
    return render(request,'vets/all_vets.html', context)
