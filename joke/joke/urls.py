from django.conf.urls import patterns, include, url
from zartomat.views import modUsersList
from zartomat.views import home
from zartomat.views import login
from zartomat.views import logout
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin[/]?', include(admin.site.urls)),
    url(r'^moduserslist[/]?$', modUsersList),
    url(r'^home[/]?$', home),
    url(r'^login[/]?$',login),
    url(r'^logout[/]?$',logout),
    url(r'', home),
    
)
