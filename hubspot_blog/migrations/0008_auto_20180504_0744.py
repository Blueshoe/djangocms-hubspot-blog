# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0007_auto_20180504_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubspotblogauthor',
            name='website',
            field=models.URLField(verbose_name='Website', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hubspotblogauthor',
            name='facebook',
            field=models.URLField(verbose_name='Facebook', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hubspotblogauthor',
            name='linkedin',
            field=models.URLField(verbose_name='LinkedIn', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hubspotblogauthor',
            name='twitter',
            field=models.URLField(verbose_name='Twitter', blank=True, null=True),
        ),
    ]
