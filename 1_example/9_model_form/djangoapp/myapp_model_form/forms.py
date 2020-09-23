from django import forms
from myapp_model_form.models import Student

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = "__all__"