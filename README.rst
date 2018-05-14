.. image:: https://badge.fury.io/py/djangocms-hubspot-blog.svg
    :target: https://badge.fury.io/py/djangocms-hubspot-blog
    
==================================
djangoCMS Hubspot Blog Integration
==================================

- Imported enitites: Authors, Topics and Posts are stored into the database
- djangoCMS App to hook views into the page (list, detail, topics-list, author-list)
- Import can be triggered by multiple ways (management command, admin, call to the api module)



Installation
==================================

- ``pip install djangocms-hubspot-blog``     
- Add the app ``djangocms_hubspot_blog`` to your ``INSTALLED_APPS``
- Add the settings listed below to your settings file
- Override the templates listed below (optional but recommended)



How to fetch blog posts
==================================
**Automatically**

The best aproach is to **automatically** fetch posts, authors and topics by
periodically running the management command ``import_blog_posts`` via CRON
or calling ``djangocms_hubspot_api.update_blog_posts()`` from a task queue.

**Manually**

You can either use the management command ``import_blog_posts`` or update all entities via a button in the admin of the blog posts.



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



Missing Functionality
==================================
- Localization (Currently it's German only)



Contributing
==================================
You're welcome to submit Pull Requests! :rocket:
Just take a look at the open issues.
