# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0004_hubspotblogpost_hubspot_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='hubspot_post_id',
            field=models.BigIntegerField(verbose_name='Hubspot Post ID'),
        ),
    ]
