# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0002_auto_20180423_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='content_html',
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True, verbose_name='Inhalt', null=True),
        ),
    ]
