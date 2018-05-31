from django import forms
from .models import organization, vacancies, categories, organization

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = organization
        exclude = ['user']
