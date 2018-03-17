from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        url(r'^introduction',views.introduction),
        url(r'^home',views.home),
        url(r'^index', views.index, name='index'),
        url(r'^form', views.form, name='form'),
  #  url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
  #  url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
  #  url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)
