from django.contrib import admin

from djangocms_hubspot_blog import hubspot_api
from djangocms_hubspot_blog.models import HubspotBlogPost, HubspotBlogAuthor, HubspotBlogTopic


def import_hubspot_posts_action(modeladmin, request, queryset):
    hubspot_api.update_blog_posts()
import_hubspot_posts_action.short_description = 'Blog Posts von Hubspot importieren'


class HubspotBlogPostInline(admin.StackedInline):
    model = HubspotBlogPost


@admin.register(HubspotBlogAuthor)
class HubspotBlogAuthorAdmin(admin.ModelAdmin):
    inlines = (HubspotBlogPostInline, )


@admin.register(HubspotBlogTopic)
class HubspotBlogTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(HubspotBlogPost)
class HubspotBlogPostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', )
    list_display = ('title', 'author', 'date_published', )
    list_filter = ('author', 'date_published', 'topics', )
    actions = (import_hubspot_posts_action, )
