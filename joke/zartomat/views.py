# encoding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from zartomat.forms import LoginForm
from django.contrib import auth




class user(object):
    def __init__ (name):
        self.name = name

def modUsersList(request):
    userlist=['aa','bb','cc']
    return HttpResponse(get_template('moduserslist.html').render(Context({'list' : userlist})))

def home(request):
    return HttpResponse(get_template('home.html').render(Context({'title':u'Żartomat', })))



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect("/loginaaa/")
        else:
            return HttpResponseRedirect("/loginsad/")
    
    if 'username' in request.session:
        return HttpResponseRedirect("/home/")
    
    return render_to_response('login.html', {
                                        "title": 'login',
                                            }, context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/logoutqwe/")
