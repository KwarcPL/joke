# encoding: utf-8
from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)
    remember = forms.BooleanField()
