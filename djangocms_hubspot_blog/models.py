from django.db import models
from djangocms_text_ckeditor.fields import HTMLField


class HubspotBlogAuthor(models.Model):
    hubspot_author_id = models.CharField('Hubspot Autor ID', primary_key=True, max_length=50, blank=False, null=False)
    hubspot_user_id = models.CharField('Hubspot User ID', max_length=50, blank=False, null=False)
    full_name = models.CharField('Name', max_length=50, blank=True, null=True)
    username = models.CharField('Benutzername', max_length=50, blank=True, null=True)
    email = models.EmailField('E-Mail', blank=True, null=True)
    facebook = models.URLField('Facebook', max_length=200, blank=True, null=True)
    linkedin = models.URLField('LinkedIn', max_length=200, blank=True, null=True)
    twitter = models.URLField('Twitter', max_length=200, blank=True, null=True)
    slug = models.CharField('Slug', max_length=200, blank=True, null=True)
    website = models.URLField('Website', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Autor'
        verbose_name_plural = 'Blog Autoren'
        ordering = ('full_name', )

    def __str__(self):
        return self.full_name


class HubspotBlogTopic(models.Model):
    id = models.CharField('ID', max_length=50, primary_key=True, blank=False, null=False)
    name = models.CharField('Name', max_length=50, blank=True, null=True)
    description = models.CharField('Beschreibung', max_length=200, blank=True, null=True)
    slug = models.CharField('Slug', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Blog Topic'
        verbose_name_plural = 'Blog Topics'
        ordering = ('name', )

    def __str__(self):
        return self.name


class HubspotBlogPost(models.Model):
    hubspot_post_id = models.BigIntegerField('Hubspot Post ID', primary_key=True, blank=False, null=False)
    title = models.CharField('Titel', max_length=200, blank=False, null=False)
    slug = models.CharField('Slug', max_length=200, blank=False, null=False)
    excerpt = HTMLField('Ausschnitt', blank=True, null=True)
    content_html = HTMLField('Inhalt', blank=True, null=True)
    meta_description = models.CharField('Meta Description', max_length=500, blank=True, null=True)
    author = models.ForeignKey(HubspotBlogAuthor, verbose_name='Autor', blank=True, null=True)
    date_published = models.DateTimeField('Datum', blank=True, null=True)
    featured_image_url = models.URLField('Featured Image', blank=True, null=True)
    topics = models.ManyToManyField(HubspotBlogTopic, verbose_name='Topics')

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ('-date_published', )

    def __str__(self):
        return self.title
