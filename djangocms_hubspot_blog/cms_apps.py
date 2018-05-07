# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class HubspotBlogApphook(CMSApp):
    app_name = 'djangocms_hubspot_blog'
    name = 'HubspotBlog'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['djangocms_hubspot_blog.urls']
