from django.contrib import admin

# Register your models here.
from .models import Pet,PetType,Owner,Food,Specialty,Vet,Visit

class PetTypeAdmin(admin.ModelAdmin):

    list_display = ['name']

admin.site.register(PetType,PetTypeAdmin)

class FoodAdmin(admin.ModelAdmin):

    list_display = ['name','calories','amount']

admin.site.register(Food,FoodAdmin)

class PetAdmin(admin.ModelAdmin):

    list_display = ['name','pettype','photo','birthday','age','weight','food']

admin.site.register(Pet,PetAdmin)

class SpecialtyAdmin(admin.ModelAdmin):

    list_display = ['name']

admin.site.register(Specialty,SpecialtyAdmin)

class VisitAdmin(admin.ModelAdmin):

    list_display = ['visit_date','description','pet']

admin.site.register(Visit,VisitAdmin)

class VetAdmin(admin.ModelAdmin):

    list_display = ['first_name','last_name']

admin.site.register(Vet,VetAdmin)

class OwnerAdmin(admin.ModelAdmin):

    list_display = ['first_name','last_name','address','city','telephone']

admin.site.register(Owner,OwnerAdmin)