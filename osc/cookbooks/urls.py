from django.conf.urls import patterns, url

from cookbooks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^newcb/$', views.newcb, name='newcb'),
    url(r'^submitncb/$', views.submitncb, name='submitncb'),
    url(r'^(?P<blog_id>\d+)/$', views.blogarticle, name='blogarticle')
)
