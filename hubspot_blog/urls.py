# -*- coding: utf-8 -*-
from django.conf.urls import url

from hubspot_blog.views import HubspotPostsList, HubspotPostDetail

urlpatterns = [
    url(r'^$', HubspotPostsList.as_view(), name='hubspot-posts-list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)$', HubspotPostDetail.as_view(), name='hubspot-post'),
]