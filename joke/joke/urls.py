from django.conf.urls import patterns, include, url
from zartomat.views import modUsersList, joke_delete, joke_edit, joke_accept, search
from zartomat.views import wait
from zartomat.views import home
from zartomat.views import login
from zartomat.views import logout
from zartomat.views import register
from zartomat.views import addjoke

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
    url(r'^wait[/]?$', wait),
    url(r'^edit/(?P<pk>\d+)$', joke_edit, name='joke_edit'),
    url(r'^delete/(?P<pk>\d+)$', joke_delete, name='joke_delete'),
    url(r'^accept/(?P<pk>\d+)$', joke_accept, name='joke_accept'),
    url(r'^search[/]?$', search),
    url(r'', home),
)
