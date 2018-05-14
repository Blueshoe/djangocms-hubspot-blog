# -*- coding: utf-8 -*-
from django.conf.urls import url

from djangocms_hubspot_blog.views import HubspotPostsList, HubspotPostDetail, HubspotTopicList, HubspotAuthorPostsList

urlpatterns = [
    url(r'^$', HubspotPostsList.as_view(), name='posts-list'),
    url(r'^topic/(?P<topic_slug>[-\w]+)$', HubspotTopicList.as_view(), name='topic-list'),
    url(r'^author/(?P<author_slug>[-\w]+)$', HubspotAuthorPostsList.as_view(), name='author-posts-list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)$', HubspotPostDetail.as_view(), name='post-detail'),
]