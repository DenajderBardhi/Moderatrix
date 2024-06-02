from django import forms
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[
        ('admin', 'Admin'),
        ('member', 'Member'),
        ('client', 'Client')
    ])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
