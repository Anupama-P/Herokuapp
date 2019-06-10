from django.conf.urls import url
from .views import SiteViewSet

site_list = SiteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

site_detail = SiteViewSet.as_view({
    'get': 'retrieve',
    'post': 'update',
    'delete': 'delete'
})

total = SiteViewSet.as_view({
    'get': 'sum'
})

average = SiteViewSet.as_view({
    'get': 'average'
})

urlpatterns = [
    url(r'^sites/$', site_list, name='site_list'),
    url(r'^sites/(?P<pk>[0-9]+)/$', site_detail, name='site_detail'),
    url(r'^summary/sum/$', total, name='sum'),
    url(r'^summary/average/$', average, name='average')
]
