from django.conf.urls import patterns, include, url
from zartomat.views import modUsersList
from zartomat.views import home
from zartomat.views import login
from zartomat.views import logout
from zartomat.views import register
from zartomat.views import addjoke
from django.views.generic import ListView
from zartomat.models import Joke

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin[/]?', include(admin.site.urls)),
    url(r'^moduserslist[/]?$', modUsersList),
    url(r'^home[/]?$', home),
    url(r'^login[/]?$',login),
    url(r'^logout[/]?$',logout),
    url(r'^register[/]?$',register),
    url(r'^addjoke[/]?$',addjoke),
    url(r'', home),
    (r'^wait/$', ListView.as_view(model=Joke,)),
)
