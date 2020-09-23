from django import forms  
from .models import Owner,Pet,Visit

class DateInput(forms.DateInput):
    input_type = 'date'


class OwnerForm(forms.ModelForm):  
    
    class Meta:  
        model = Owner  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class PetForm(forms.ModelForm):  
    
    class Meta:  
        model = Pet  
        fields = "__all__"
        widgets = {'birthday': DateInput()}

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class VisitForm(forms.ModelForm):  
    
    class Meta:  
        model = Visit  
        fields = "__all__" 
        widgets = {'visit_date': DateInput()}

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'