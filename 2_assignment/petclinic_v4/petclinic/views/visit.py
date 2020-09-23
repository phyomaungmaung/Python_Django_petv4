from ..models import Visit,Pet
from ..forms import VisitForm  
from django.shortcuts import render, redirect

def add_visit(request, pet_id):  
    pet = Pet.objects.get(id=pet_id)  
    owner_id = pet.owner_id.id

    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect("/petclinic/owners/" + str(owner_id) + '/')
    else:  
        form = VisitForm(initial={'pet': pet_id})  
    return render(request,'visit/add.html',{'form':form})