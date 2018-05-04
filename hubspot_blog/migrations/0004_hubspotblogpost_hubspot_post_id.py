# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0003_auto_20180423_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubspotblogpost',
            name='hubspot_post_id',
            field=models.IntegerField(verbose_name='Hubspot Post ID', default=1),
            preserve_default=False,
        ),
    ]
