from ..models import Owner
from django.shortcuts import render

# Create your views here.

def owner(request,owner_id):
    owner = Owner.objects.get(pk=owner_id)
    return render(request,'owners/detail.html', {'owner': owner})

def all_owners(request):
    if 'last_name' in request.GET:
        all_owners = Owner.objects.filter(last_name__icontains=request.GET['last_name'])
    else:
        all_owners = Owner.objects.all()
    context = { "all_owners": all_owners }
    return render(request,'owners/list.html', context)

def find_owner(request):
    return render(request,'owners/find.html', {})

