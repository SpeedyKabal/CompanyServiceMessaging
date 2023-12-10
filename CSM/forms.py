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


    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Assuming you want to allow only digits and limit to 10 characters
        return ''.join(filter(str.isdigit, phone))[:10]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']


    def clean_last_name(self):
        return self.cleaned_data['last_name'].upper()


    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return ' '.join([word.capitalize() for word in first_name.split()])
    

    def clean_username(self):
        return self.cleaned_data['username'].lower()


