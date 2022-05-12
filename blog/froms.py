from django.db import models
from django.forms import ModelForm, fields
from .models import Blogs , Profile

class addblogform(ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','details','image','writer','tags']

class edit_profile(ModelForm):
    class Meta:
         model = Profile
         fields = '__all__' 


        

