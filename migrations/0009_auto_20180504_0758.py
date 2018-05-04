# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0008_auto_20180504_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hubspotblogauthor',
            options={'ordering': ('full_name',), 'verbose_name_plural': 'Blog Autoren', 'verbose_name': 'Blog Autor'},
        ),
        migrations.AlterModelOptions(
            name='hubspotblogtopic',
            options={'ordering': ('name',), 'verbose_name_plural': 'Blog Topics', 'verbose_name': 'Blog Topic'},
        ),
    ]
