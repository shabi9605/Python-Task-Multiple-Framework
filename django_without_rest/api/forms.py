
from django import forms
from django.core import validators

def validate_a(a):
    if a == 0:
        raise forms.ValidationError("The value of a not equal to zero") 
    
    

class QuadraticForm(forms.Form):
    a = forms.FloatField(required=True,validators=[validate_a])
    b = forms.FloatField(required=True,)
    c = forms.FloatField(required=True,)