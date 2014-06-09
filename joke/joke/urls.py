from django.conf.urls import patterns, include, url
from zartomat.views import modUsersList
from zartomat.views import home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'joke.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^moduserslist/', modUsersList),
    url(r'^home/', home),
    url(r'^/', home),
    
)
