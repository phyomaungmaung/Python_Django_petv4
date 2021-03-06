"""petclinic_v4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from petclinic import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('petclinic/', views.index),
    path('petclinic/owners/', views.all_owners),
    path('petclinic/owners/find/', views.find_owner),
    path('petclinic/owners/<int:owner_id>/', views.owner),
    path('petclinic/vets/', views.all_vets),
    path('petclinic/pets/add/<int:owner_id>/', views.add_pet),
    path('petclinic/visit/add/<int:pet_id>/', views.add_visit)
]