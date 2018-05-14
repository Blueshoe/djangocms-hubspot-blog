from django.conf import settings
from django.views.generic import ListView, DetailView
from djangocms_hubspot_blog.models import HubspotBlogPost


class HubspotPostsList(ListView):
    model = HubspotBlogPost
    paginate_by = settings.get('HUBSPOT_BLOG_PAGE_LIMIT', default=10)
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
