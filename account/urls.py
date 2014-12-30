from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wmbank.views.home', name='home'),
    url(r'^$', views.index),
    url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
 url(r'^register/$', views.register, name='register'),
    url(r'^add_transaction/$', views.add_transaction),
	url(r'^profile/$', views.profile),
    #url(r'^(?P<username>\w+)$', views.account_details),
    

   
)
