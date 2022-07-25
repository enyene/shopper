from dataclasses import field
from django import forms
from django.contrib.auth.models import User

from products.models import comment






class UserForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields= ('username','first_name','last_name','email','Password')

# class commentForm(forms.ModelForm):
#     class Meta:
#         model=comment
#         field ='__all__'