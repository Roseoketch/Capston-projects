from django import forms
from .models import Contact,  Organization, Program

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Organization
        exclude = ['user']
