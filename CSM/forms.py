from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Employee


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']


