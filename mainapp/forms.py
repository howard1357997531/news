from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class AccountsettingForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name','first_name','phone','email','address','picture']

class CreateNewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['press',]

class UpdateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

