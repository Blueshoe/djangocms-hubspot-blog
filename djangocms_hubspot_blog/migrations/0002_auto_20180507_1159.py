# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_hubspot_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='topics',
            field=models.ManyToManyField(to='djangocms_hubspot_blog.HubspotBlogTopic', verbose_name=b'Topics', blank=True),
        ),
    ]
