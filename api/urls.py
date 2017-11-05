from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import cluster_views, osd_views, pool_views, crush_views, rule_views
urlpatterns = [
    #url(r'^cluster/$', cluster_views.ClusterList.as_view()),
    #url(r'^cluster/(?P<pk>[0-9]+)/$', cluster_views.ClusterDetail.as_view()),
    url(r'^cluster-capacity/(?P<pk>[0-9]+)/$', cluster_views.ClusterCapacityList.as_view()),
    url(r'^osd/(?P<pk>[0-9]+)/$', osd_views.OsdList.as_view()),
    url(r'^odsProperty/(?P<pk>[0-9]+)/$', osd_views.OsdPropertyList.as_view()),
    url(r'^osd-capacity/(?P<pk>[0-9]+)/$', osd_views.OsdCapacityList.as_view()),
    url(r'^pool/(?P<pk>[0-9]+)/$', pool_views.PoolList.as_view()),
    url(r'^pool-capacity/(?P<pk>[0-9]+)/$', pool_views.PoolCapacityList.as_view()),
    url(r'^crush/(?P<pk>[0-9]+)/$', crush_views.CrushList.as_view()),
    url(r'^rule/(?P<pk>[0-9]+)/$', rule_views.RuleList.as_view()),
    url(r'rbd/(?P<pk>[0-9]+)/$', pool_views.RBDList.as_view())
]