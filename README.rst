.. image:: https://badge.fury.io/py/djangocms-hubspot-blog.svg
    :target: https://badge.fury.io/py/djangocms-hubspot-blog
    
==================================
djangoCMS Hubspot Blog Integration
==================================

- Management command to fetch Authors, Topics and Posts and store them in the database    
- djangoCMS App to hook list and detail view into a page

Installation
==================================

- ``pip install djangocms-hubspot-blog``     
- Add the app ``djangocms_hubspot_blog`` to your ``INSTALLED_APPS``
- Add the settings listed below to your settings file
- Override the templates listed below

Settings
==================================

+-------------------------+----------+---------------+
| Setting Name            | Required | Default Value |
+=========================+==========+===============+
| HUBSPOT_API_KEY         | yes      | /             |
+-------------------------+----------+---------------+
| HUBSPOT_BLOG_ID         | yes      | /             |
+-------------------------+----------+---------------+
| PORTAL_ID               | yes      | /             |
+-------------------------+----------+---------------+
| HUBSPOT_BLOG_PAGE_LIMIT | no       | 10            |
+-------------------------+----------+---------------+

Views & Templates
==================================
It's recommended to override the given templates. Take a look at the templates on how to do it.

+------------------------+---------------------------------------------+--------------------------------------------+
| View                   | View Name                                   | Template                                   |
+========================+=============================================+============================================+
| HubspotPostsList       | ``djangocms_hubspot_blog:posts-list``       | ``djangocms_hubspot_blog/post_list.html``  |
+------------------------+---------------------------------------------+--------------------------------------------+
| HubspotTopicList       | ``djangocms_hubspot_blog:topic-list``       | ``djangocms_hubspot_blog/post_list.html``  |
+------------------------+---------------------------------------------+--------------------------------------------+
| HubspotAuthorPostsList |``djangocms_hubspot_blog:author-posts-list`` | ``djangocms_hubspot_blog/post_list.html``  |
+------------------------+---------------------------------------------+--------------------------------------------+
| HubspotPostDetail      | ``djangocms_hubspot_blog:post-detail``      | ``djangocms_hubspot_blog/post_detail.html``|
+------------------------+---------------------------------------------+--------------------------------------------+

The pagination has an additional partial template at ``djangocms_hubspot_blog/partials/pagination.html``

How to fetch blog posts
-----------------------
**Automatically**

The best aproach is to **automatically** fetch posts, authors and topics by
periodically running the management command ``import_blog_posts`` via CRON
or calling ``djangocms_hubspot_api.update_blog_posts()`` from a task queue.

**Manually**

However, it's also possible for site editors to **manually** trigger an update via a button in the admin.

Missing Functionality
------------------------- 
- Localization (Currently it's German only)

Contributing
----------------
You're welcome to submit Pull Requests! :rocket:
Just take a look at the open issues.
