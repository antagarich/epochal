# coding: utf
from django.conf.urls import patterns, url
from django.conf import settings
from vkrm import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(),name = 'index'),
                       url(r'^states/$', views.States.as_view(),name = 'states'),
                       url(r'^personalities/$', views.Personalities.as_view(), name='personalities'),
                       url(r'^events/$', views.Events.as_view(),name = 'events'),
                       url(r'^wonders/$', views.Wonders.as_view(),name ='wonders'),
                       url(r'^discoveries/$', views.Discoveries.as_view(),name='discoveries'),
                       url(r'^articles/$', views.Articles.as_view(),name='articles'),
                       url(r'^states/(?P<pk>\d+)/$', views.DetailState.as_view(),name='detail_state'),
                       url(r'^(?P<pk>\d+)/$', views.DetailAge.as_view(),name='detail_age'),
                       url(r'^personalities/(?P<pk>\d+)/$', views.DetailPersonality.as_view(),name='detail_personality'),
                       url(r'^events/(?P<pk>\d+)/$', views.DetailEvent.as_view(),name='detail_event'),
                       url(r'^discoveries/(?P<pk>\d+)/$', views.DetailDiscovery.as_view(),name='detail_discovery'),
                       url(r'^articles/(?P<pk>\d+)/$', views.DetailArticle.as_view(),name='detail_article'),
                       url(r'^wonders/(?P<pk>\d+)/$', views.DetailWonder.as_view(),name='detail_wonder'),
                       url(r'^work/$', views.WorkView,name='work'),
                       url(r'^login/$', views.login,name='login'),
                       url(r'^logout/$',views.logout,name='logout'),
                       url(r'^register/$', views.register,name='register'),
                       url(r'^addArticle/$', views.addArticle,name='addArticle'),
                       url(r'^editArticle/(?P<pk>\d+)/$', views.editArticle,name='editArticle'),
                       url(r'^deleteArticle/(?P<pk>\d+)/$', views.deleteArticle,name='deleteArticle'),)
if settings.DEBUG:
    urlpatterns += patterns('',(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))