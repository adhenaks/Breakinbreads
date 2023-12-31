from django import forms
from bakery.models import User,Category
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","address"]


class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["caketype"]

