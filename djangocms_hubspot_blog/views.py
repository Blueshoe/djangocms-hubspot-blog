from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

import hubspot_api
from djangocms_hubspot_blog.models import HubspotBlogPost


class HubspotPostsList(ListView):
    model = HubspotBlogPost
    paginate_by = getattr(settings, 'HUBSPOT_BLOG_PAGE_LIMIT', 10)
    context_object_name = 'posts'
    template_name = 'djangocms_hubspot_blog/post_list.html'


class HubspotPostDetail(DetailView):
    model = HubspotBlogPost
    context_object_name = 'post'
    template_name = 'djangocms_hubspot_blog/post_detail.html'


class HubspotTopicList(HubspotPostsList):
    def get_queryset(self):
        topic_slug = self.kwargs.get('topic_slug')
        return self.model.objects.filter(topics__slug__in=[topic_slug])


class HubspotAuthorPostsList(HubspotPostsList):
    def get_queryset(self):
        author_slug = self.kwargs.get('author_slug')
        return self.model.objects.filter(author__slug__in=[author_slug])


@staff_member_required
def update_hubspot_blog_posts(request):
    hubspot_api.update_blog_posts()
    messages.add_message(request, messages.INFO, 'Hubspot Blog Posts wurden aktualisiert')
    return redirect(reverse('admin:djangocms_hubspot_blog_hubspotblogpost_changelist'))
