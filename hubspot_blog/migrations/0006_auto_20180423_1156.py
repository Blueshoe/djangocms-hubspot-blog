# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hubspot_blog', '0005_auto_20180423_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubspotblogpost',
            name='excerpt',
            field=djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True, verbose_name='Ausschnitt'),
        ),
    ]
