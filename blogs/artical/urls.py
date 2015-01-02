from django.conf.urls import patterns, url

from artical import views

urlpatterns = patterns('',
    url(r'^$', views.myviewclass.listPosts, name='listPosts'),
    url(r'^detail/$', views.myviewclass.detail, name='detail'),
    url(r'^addpost/$', views.myviewclass.addpost, name='addpost'),
    url(r'^updateartical/$', views.myviewclass.updateartical, name='updateartical'),

    url(r'^addcomment/$', views.myviewclass.addcomment, name='addcomment'),
    url(r'^(?P<artical_id>\d+)/articledetail/$', views.myviewclass.articledetail, name='articledetail'),

    url(r'^(?P<artical_id>\d+)/editartical/$', views.myviewclass.editartical, name='editartical'),
    url(r'^(?P<artical_id>\d+)/deleteartical/$', views.myviewclass.deleteartical, name='deleteartical'),

)