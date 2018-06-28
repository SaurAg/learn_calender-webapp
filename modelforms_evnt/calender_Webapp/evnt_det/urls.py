from django.conf.urls import url
from evnt_det import views
 
app_name = 'evnt_det'
 
urlpatterns = [
    # /modelforms/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^evn/detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # modelforms/product/entry
    url(r'^evn/entry/$',views.EventEntry.as_view(),name='event-entry'),
 
    # modelforms/product/2
    url(r'^evn/(?P<pk>[0-9]+)/$', views.EventUpdate.as_view(), name='event-update'),
 
    # modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'^evn/(?P<pk>[0-9]+)/delete$', views.EventDelete.as_view(), name='event-delete'), 
]