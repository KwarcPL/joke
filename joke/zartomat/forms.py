# encoding: utf-8
from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)
    remember = forms.BooleanField()


class AddJokeForm(forms.Form):
    joke = forms.CharField(max_length=1000, widget=forms.Textarea, label="")
    tags = forms.CharField(max_length=100, label="tags:")

class SearchForm(forms.Form):
    tags = forms.CharField(max_length=100, label="tags:")
    author = forms.CharField(max_length=50, label = 'author:')
    rate = forms.IntegerField(label = 'rate:')
    accepted = forms.BooleanField(label = 'accepted:')

