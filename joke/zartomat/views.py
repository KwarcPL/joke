from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def modUsersList(request):
    return HttpResponse(get_template('moduserslist.html').render(Context({'msg' : 'haha'})))

def home(request):
    return HttpResponse(get_template('home.html').render(Context({'msg' : 'bb'})))
