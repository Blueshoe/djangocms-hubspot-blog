# -*- coding: utf-8 -*-
import json

import datetime
import traceback

import requests
from django.conf import settings
from requests import HTTPError

from djangocms_hubspot_blog.models import HubspotBlogPost, HubspotBlogTopic, HubspotBlogAuthor

API_BASE_URL = 'https://api.hubapi.com'
API_KEY = settings.HUBSPOT_API_KEY
BLOG_ID = settings.HUBSPOT_BLOG_ID
PORTAL_ID = settings.HUBSPOT_PORTAL_ID
try:
    PAGE_LIMIT = settings.HUBSPOT_BLOG_PAGE_LIMIT
except AttributeError:
    PAGE_LIMIT = 10


def get_blog_posts(page=1, limit=PAGE_LIMIT, as_list=False):
    path = '/content/api/v2/blog-posts'
    url = '{base}{path}?hapikey={api_key}&content_group_id={blog_id}&order_by=publish_date&limit={limit}offset={offset}&state=PUBLISHED'.format(
        base=API_BASE_URL,
        path=path,
        api_key=API_KEY,
        blog_id=BLOG_ID,
        limit=limit,
        offset=limit * page - limit
    )
    try:
        print('Fetching blog posts from hubspot...')
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as error:
        print('get_blog_posts() api error:')
        print(error)
        return None
    else:
        if as_list:
            return r.json().get('objects')
        return r.json()


def get_blog_post(id):
    path = '/content/api/v2/blog-posts'
    url = '{base}{path}/{post_id}?hapikey={api_key}'.format(
        base=API_BASE_URL,
        path=path,
        post_id=id,
        api_key=API_KEY
    )
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as error:
        print('get_blog_post() api error:')
        print(error)
        return None
    else:
        return r.json()


def get_topics():
    path = '/blogs/v3/topics'
    url = '{base}{path}?hapikey={api_key}&{limit}'.format(
        base=API_BASE_URL,
        path=path,
        api_key=API_KEY,
        limit=1000
    )
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as error:
        print('get_topics() api error:')
        print(error)
        return None
    else:
        return r.json()


def _import_topics():
    topics_json = get_topics()
    for topic in topics_json.get('objects'):
        if topic['portalId'] != PORTAL_ID:
            continue
        HubspotBlogTopic.objects.update_or_create(id=topic['id'], defaults={
            'name': topic['name'],
            'description': topic['description'],
            'slug': topic['slug'],
        })


def _import_blog_posts():
    posts = get_blog_posts(limit=100000, as_list=True)
    for post in posts:
        try:
            # Get or create the post's author
            author_field = post['blog_author']
            author, _ = HubspotBlogAuthor.objects.update_or_create(
                hubspot_author_id=post['blog_author_id'],
                defaults={
                    'full_name': author_field['full_name'],
                    'hubspot_user_id': post['author_user_id'],
                    'username': author_field['username'],
                    'email': author_field['email'],
                    'facebook': author_field['facebook'],
                    'linkedin': author_field['linkedin'],
                    'twitter': author_field['twitter'],
                    'slug': author_field['slug'],
                    'website': author_field['website'],
                }
            )
            # Get or create the post object itself
            blog_post, _ = HubspotBlogPost.objects.update_or_create(
                hubspot_post_id=post['id'],
                defaults={
                    'title': post['html_title'],
                    'slug': post['slug'],
                    'excerpt': post['post_summary'],
                    'content_html': post['post_body'],
                    'author': author,
                    # Hubspot returns ms timestamp, fromtimestamp() expects seconds
                    'date_published': datetime.datetime.fromtimestamp(post['publish_date'] / 1000),
                    'meta_description': post['meta_description'],
                    'featured_image_url': post['featured_image'],
                }
            )
            # Add topics to post
            for topic_id in post['topic_ids']:
                topic = HubspotBlogTopic.objects.get(id=topic_id)
                if topic:
                    blog_post.topics.add(topic)
            blog_post.save()

        except Exception:
            print('Error fetching a post')
            traceback.print_exc()


def update_blog_posts():
    _import_topics()
    _import_blog_posts()
