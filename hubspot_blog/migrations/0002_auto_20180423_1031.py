# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hubspotblogpost',
            options={'verbose_name_plural': 'Blog Posts', 'ordering': ('-date_published',), 'verbose_name': 'Blog Post'},
        ),
    ]
