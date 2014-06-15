# encoding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from zartomat.forms import LoginForm, AddJokeForm, SearchForm
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser, Permission
from zartomat.models import Joke
from datetime import date

class user(object):
    def __init__ (name):
        self.name = name

def modUsersList(request):
    userlist=['aa','bb','cc']
    return HttpResponse(get_template('moduserslist.html').render(Context({'list' : userlist})))

def home(request):
    jokes = Joke.objects.all()
    if isinstance(request.user,AnonymousUser):
        return HttpResponse(get_template('home.html').render(Context({'title':'Żartomat', "user": "" , 'state':'0', 'jokes' : jokes, 'accepted' : 1})))
    else:    
        return HttpResponse(get_template('home.html').render(Context({'title':'Żartomat', "user" : request.user.get_username(),'state' :'1', 'jokes' : jokes, 'accepted' : 1})))

def wait(request):
    jokes = Joke.objects.all()
    for joke in jokes:
        joke.published_date = date.isoformat(joke.published_date)

    if  isinstance(request.user,AnonymousUser):
        return render_to_response('wait.html', {
                                        'state': '0',
                                        "title" : 'Poczekalnia',
                                        'accepted': 0,
                                        'user' : "",
                                        'jokes' : jokes
                                            }, context_instance=RequestContext(request))


        
    else:    
        return render_to_response('wait.html', {
                                        'state': '1',
                                        'title': 'Poczeklania',
                                        'accepted': 0,
                                        'user' : request.user.get_username(),
                                        'jokes': jokes
                                            }, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/loginaaa/")
        else:
            return HttpResponseRedirect("/loginsad/")

    if not isinstance(request.user,AnonymousUser):
        return HttpResponseRedirect("/home/")

    return render_to_response('login.html', {
                                        "title": 'login',
                                        "state": '0',
                                            }, context_instance=RequestContext(request))


def register(request):
    if not isinstance(request.user,AnonymousUser) :
        return HttpResponseRedirect("/home/")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            permission = Permission.objects.get(codename='add_joke')
            new_user.user_permissions.add(permission)
            return HttpResponseRedirect("/newuser/")
    else:
        form = UserCreationForm()
    return render_to_response('register.html', {
                                        "state": '0',
                                        "form": form,
                                            }, context_instance=RequestContext(request))

def addjoke(request):
    if  isinstance(request.user,AnonymousUser) :
        return HttpResponseRedirect("/home/")

    if request.method == 'POST':
        form = AddJokeForm(request.POST)
        if form.is_valid():
            newjoke = Joke()
            newjoke.joke_text = form.cleaned_data['joke']
            newjoke.tags = form.cleaned_data['tags']
            newjoke.accepted = 0
            newjoke.rate = 0
            newjoke.number_of_grades = 0
            newjoke.author = request.user.get_username()
            newjoke.published_date = date.today()
            newjoke.save()
        return HttpResponseRedirect("/home/")
    else:
        form = AddJokeForm()
    return render_to_response('addjoke.html', {
                                        "state": '1',
                                        "form": form,
                                            }, context_instance=RequestContext(request))

  


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/logoutqwe/")

def joke_edit(request, pk):
    joke = Joke.objects.get(id = pk)
    if request.method == 'POST':
        form = AddJokeForm(request.POST)
        if form.is_valid():
            joke.joke_text = form.cleaned_data['joke']
            joke.tags =  form.cleaned_data['tags']
            joke.save()
        return HttpResponseRedirect("/home/")
    else:
        form = AddJokeForm()
    return render_to_response('addjoke.html', {
                                        "state": '1',
                                        "form": form,
                                            }, context_instance=RequestContext(request))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def joke_delete(request, pk):
    joke = Joke.objects.get(id = pk)
    joke.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def joke_accept(request, pk):
    joke = Joke.objects.get(id = pk)
    joke.accepted = not joke.accepted
    joke.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        tags = ''
        author = ''
        rate = 0
        accepted = 0
        if(form.data.has_key('tags')):
            tags = form.data['tags']
        if(form.data.has_key('author')):
            author = form.data['author']
        if(form.data.has_key('rate')):
            rate = form.data['rate']
        if(form.data.has_key('accepted')):
            accepted = form.data['accepted']
        jokes = Joke.objects.all()
        if isinstance(request.user,AnonymousUser):
            return HttpResponse(get_template('list.html').render(Context({'title':'Żartomat', "user": '' , 'state': '0', 'jokes' : jokes, 'accepted' : accepted})))
        else:
            return HttpResponse(get_template('list.html').render(Context({'title':'Żartomat', "user" : request.user.get_username(),'state' :'1', 'jokes' : jokes, 'accepted' : accepted})))
    else:
        form = SearchForm()
    if isinstance(request.user,AnonymousUser):
        return render_to_response('search.html', {
                                        "state": '0',
                                        "form": form,
                                            }, context_instance=RequestContext(request))
    else:
        return render_to_response('search.html', {
                                        "state": '1',
                                        "form": form,
                                            }, context_instance=RequestContext(request))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
