# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0012_auto_20141012_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='summary',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='summary',
            field=ckeditor.fields.RichTextField(null=True, blank=True),
        ),
    ]
