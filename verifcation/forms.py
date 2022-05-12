from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
class Meta:
       model = User
       fields = ['username','email','password1','password2']  

class EditProfileForm(UserChangeForm):
    username   = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    first_name =forms.CharField(max_length=200)
    last_name  =  forms.CharField(max_length=200)
    date_joined =forms.CharField(max_length=200)

class Meta:
       model = User
       fields = ['id_username','id_email','id_first_name']   