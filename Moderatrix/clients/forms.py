from django import forms
from .models import Client, ClientProject

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']

class ClientProjectForm(forms.ModelForm):
    class Meta:
        model = ClientProject
        fields = ['client', 'project_name', 'description', 'tasks']
