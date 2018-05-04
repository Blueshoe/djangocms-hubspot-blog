# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HubspotBlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Titel', max_length=200)),
                ('slug', models.CharField(verbose_name='Slug', max_length=200)),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='Ausschnitt')),
                ('content_html', models.TextField(blank=True, null=True, verbose_name='Inhalt')),
                ('author', models.CharField(blank=True, null=True, verbose_name='Autor', max_length=200)),
                ('date_published', models.DateTimeField(blank=True, null=True, verbose_name='Datum')),
            ],
        ),
    ]
