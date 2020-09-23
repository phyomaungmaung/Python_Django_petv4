from django import forms  
from .models import Owner,Pet,Visit

class DateInput(forms.DateInput):
    input_type = 'date'

class OwnerForm(forms.ModelForm):  
    
    class Meta:  
        model = Owner  
        fields = "__all__"  

class PetForm(forms.ModelForm):  
    
    class Meta:  
        model = Pet  
        fields = "__all__"
        widgets = {'birthday': DateInput()}

class VisitForm(forms.ModelForm):  
    
    class Meta:  
        model = Visit  
        fields = "__all__" 
        widgets = {'visit_date': DateInput()}