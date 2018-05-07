# -*- coding: utf-8 -*-
from django.core.management import BaseCommand

from djangocms_hubspot_blog import hubspot_api
from djangocms_hubspot_blog.models import HubspotBlogPost


class Command(BaseCommand):
    help = 'Imports posts from hubspot'

    def handle(self, *args, **options):
        hubspot_api.update_blog_posts()
        num_posts = HubspotBlogPost.objects.count()
        self.stdout.write('Import done, {} posts in database'.format(num_posts))
