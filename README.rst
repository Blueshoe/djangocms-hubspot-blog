.. image:: https://badge.fury.io/py/djangocms-hubspot-blog.svg
    :target: https://badge.fury.io/py/djangocms-hubspot-blog
    
==================================
djangoCMS Hubspot Blog Integration
==================================

- Management command to fetch Authors, Topics and Posts and store them in the database    
- djangoCMS App to hook list and detail view into a page

Usage
==================================

- `pip install djangocms-hubspot-blog`     
- Add the app `hubspot_blog` to your `INSTALLED_APPS`    
- Optionally override the two templates `hubspot_blog/[post_list.html,post_detail.html]`    

How to fetch blog posts
-----------------------
**Automatically**

The best aproach is to **automatically** fetch posts, authors and topics by
periodically running the management command `import_blogposts` via CRON
or calling `hubspot_api.update_blog_posts()` from a task queue.

**Manually**

However, it's also possible for site editors to **manually** trigger an
update via an admin action (it's needed to select a blog post in order
to run the action, so for the first time use, run the management command or create a dummy blog post via the admin)

Missing Functionality
-------------------------
- Author page    
- Topic page    

Contributing
----------------
You're welcome to submit Pull Requests! :rocket:
Just take a look at the open issues.
