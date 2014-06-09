from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

class user(object):
    def __init__ (name):
        self.name = name



def modUsersList(request):
    userlist=['aa','bb','cc']
    return HttpResponse(get_template('moduserslist.html').render(Context({'list' : userlist})))

def home(request):
    return HttpResponse(get_template('home.html').render(Context({'list' : html})))
