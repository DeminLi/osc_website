from django.conf.urls import patterns, url

from register import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/done/$', views.done, name='done'),
)
