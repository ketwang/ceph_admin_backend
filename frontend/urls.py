from django.conf.urls import url

from . import  views
urlpatterns = [
    url(r'^getCluster/$', views.getAllCluster),
    url(r'^getClusterCapac/(?P<pk>[0-9]+)', views.getClusterCapac),
    url(r'^getPools/(?P<pk>[0-9]+)', views.getPools),
    url(r'^getOsds/(?P<pk>[0-9]+)', views.getOSDs),
    url(r'^getCrush/(?P<pk>[0-9]+)', views.getCrush),
    url(r'^getCrushTree/(?P<pk>[0-9]+)', views.getCrushTree),
    url(r'^getImages/(?P<pk>[0-9]+)', views.getImages),
]