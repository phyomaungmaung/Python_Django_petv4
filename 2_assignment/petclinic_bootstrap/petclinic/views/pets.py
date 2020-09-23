from ..models import Pet
from ..forms import PetForm  
from django.shortcuts import render, redirect

def add_pet(request, owner_id):  
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect("/petclinic/owners/" + str(owner_id) + '/') 
    else:
        form = PetForm(initial={'owner_id': owner_id})  
    return render(request,'pets/add.html',{'form':form})