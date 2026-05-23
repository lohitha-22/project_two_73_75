
from django import forms

from app1.models import student

class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'


        

class student_delete_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
