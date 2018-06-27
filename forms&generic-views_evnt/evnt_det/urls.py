from django.conf.urls import url

from evnt_det import views

app_name = 'evnt_det'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),
    url(r'^makeentry$', views.makeentry, name='entry'),
]