# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0009_auto_20180504_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='topics',
            field=models.ManyToManyField(to='hubspot_blog.HubspotBlogTopic', blank=True, verbose_name='Topics'),
        ),
    ]
