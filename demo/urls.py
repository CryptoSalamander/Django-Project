from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from . import views
urlpatterns = [
    url( r'^demo$', views.index),
    url( r'^$', views.select),
    url( r'^items/(?P<number>\d+)/$', views.showitem),
    url( r'^items/(?P<number>\d+)/info$', views.info),
    url( r'^items/(?P<number>\d+)/buy$', views.buy),
    url( r'^items/(?P<number>\d+)/buy/pay$', views.pay),
    url( r'^items/(?P<number>\d+)/buy/card$', views.card),
    url( r'^items/(?P<number>\d+)/buy/cash$', views.cash),
    url( r'^items/(?P<number>\d+)/buy/done$', views.done),
    url( r'^demo/register/$',views.register),
    url( r'^demo/register/done$', views.registerdone ),
    url(r'^demo/login/','django.contrib.auth.views.login',
    name='login', kwargs={'template_name': 'demo/login.html'}),
    url( r'^demo/logout/', 'django.contrib.auth.views.logout', name='logout', kwargs={'template_name' : 'demo/logout.html'}),
]
