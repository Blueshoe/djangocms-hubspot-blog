# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0006_auto_20180423_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubspotBlogAuthor',
            fields=[
                ('hubspot_author_id', models.CharField(verbose_name='Hubspot Autor ID', max_length=50, serialize=False, primary_key=True)),
                ('hubspot_user_id', models.CharField(max_length=50, verbose_name='Hubspot User ID')),
                ('full_name', models.CharField(blank=True, max_length=50, verbose_name='Name', null=True)),
                ('username', models.CharField(blank=True, max_length=50, verbose_name='Benutzername', null=True)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail', null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, verbose_name='Facebook', null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, verbose_name='LinkedIn', null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, verbose_name='Twitter', null=True)),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='Slug', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HubspotBlogTopic',
            fields=[
                ('id', models.CharField(verbose_name='ID', max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name', null=True)),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Beschreibung', null=True)),
                ('slug', models.CharField(blank=True, max_length=50, verbose_name='Slug', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='hubspotblogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='hubspotblogpost',
            name='featured_image_url',
            field=models.URLField(blank=True, verbose_name='Featured Image', null=True),
        ),
        migrations.AddField(
            model_name='hubspotblogpost',
            name='meta_description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Meta Description', null=True),
        ),
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='author',
            field=models.ForeignKey(to='hubspot_blog.HubspotBlogAuthor', blank=True, verbose_name='Autor', null=True),
        ),
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='hubspot_post_id',
            field=models.BigIntegerField(verbose_name='Hubspot Post ID', serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='hubspotblogpost',
            name='topics',
            field=models.ManyToManyField(blank=True, verbose_name='Topics', to='hubspot_blog.HubspotBlogTopic', null=True),
        ),
    ]
