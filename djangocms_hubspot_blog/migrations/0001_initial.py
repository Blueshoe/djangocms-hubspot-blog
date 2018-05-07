# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HubspotBlogAuthor',
            fields=[
                ('hubspot_author_id', models.CharField(max_length=50, serialize=False, verbose_name=b'Hubspot Autor ID', primary_key=True)),
                ('hubspot_user_id', models.CharField(max_length=50, verbose_name=b'Hubspot User ID')),
                ('full_name', models.CharField(max_length=50, null=True, verbose_name=b'Name', blank=True)),
                ('username', models.CharField(max_length=50, null=True, verbose_name=b'Benutzername', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'E-Mail', blank=True)),
                ('facebook', models.URLField(null=True, verbose_name=b'Facebook', blank=True)),
                ('linkedin', models.URLField(null=True, verbose_name=b'LinkedIn', blank=True)),
                ('twitter', models.URLField(null=True, verbose_name=b'Twitter', blank=True)),
                ('slug', models.CharField(max_length=200, null=True, verbose_name=b'Slug', blank=True)),
                ('website', models.URLField(null=True, verbose_name=b'Website', blank=True)),
            ],
            options={
                'ordering': ('full_name',),
                'verbose_name': 'Blog Autor',
                'verbose_name_plural': 'Blog Autoren',
            },
        ),
        migrations.CreateModel(
            name='HubspotBlogPost',
            fields=[
                ('hubspot_post_id', models.BigIntegerField(serialize=False, verbose_name=b'Hubspot Post ID', primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Titel')),
                ('slug', models.CharField(max_length=200, verbose_name=b'Slug')),
                ('excerpt', djangocms_text_ckeditor.fields.HTMLField(null=True, verbose_name=b'Ausschnitt', blank=True)),
                ('content_html', djangocms_text_ckeditor.fields.HTMLField(null=True, verbose_name=b'Inhalt', blank=True)),
                ('meta_description', models.CharField(max_length=500, null=True, verbose_name=b'Meta Description', blank=True)),
                ('date_published', models.DateTimeField(null=True, verbose_name=b'Datum', blank=True)),
                ('featured_image_url', models.URLField(null=True, verbose_name=b'Featured Image', blank=True)),
                ('author', models.ForeignKey(verbose_name=b'Autor', blank=True, to='djangocms_hubspot_blog.HubspotBlogAuthor', null=True)),
            ],
            options={
                'ordering': ('-date_published',),
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='HubspotBlogTopic',
            fields=[
                ('id', models.CharField(max_length=50, serialize=False, verbose_name=b'ID', primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name=b'Name', blank=True)),
                ('description', models.CharField(max_length=200, null=True, verbose_name=b'Beschreibung', blank=True)),
                ('slug', models.CharField(max_length=50, null=True, verbose_name=b'Slug', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Blog Topic',
                'verbose_name_plural': 'Blog Topics',
            },
        ),
        migrations.AddField(
            model_name='hubspotblogpost',
            name='topics',
            field=models.ManyToManyField(to='djangocms_hubspot_blog.HubspotBlogTopic', verbose_name=b'Topics'),
        ),
    ]
