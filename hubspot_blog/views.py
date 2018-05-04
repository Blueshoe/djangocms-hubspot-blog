from django.views.generic import ListView, DetailView
from hubspot_blog.models import HubspotBlogPost


class HubspotPostsList(ListView):
    model = HubspotBlogPost
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'hubspot_blog/post_list.html'


class HubspotPostDetail(DetailView):
    model = HubspotBlogPost
    context_object_name = 'post'
    template_name = 'hubspot_blog/post_detail.html'
