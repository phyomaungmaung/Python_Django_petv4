from django.shortcuts import render

# Create your views here.
class Owner:
    def __init__(self, first_name, last_name, address, city, telephone):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.telephone = telephone

def index(request):
    owner1 = Owner('Kyaw','Kyaw','Kyeemyindine','Yangon','12345')
    owner2 = Owner('Aung','Aung','Ahlone','Yangon','001279')
    owner_list = [owner1,owner2]
    context = { "owner_list": owner_list }
    return render(request,'6_index_ttable.html',context)
    # render(request, html_file, context)