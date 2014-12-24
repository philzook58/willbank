from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wmbank.views.home', name='home'),
    url(r'^$', views.index),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^(?P<username>\w+)$', views.account_details),
    

   
)
