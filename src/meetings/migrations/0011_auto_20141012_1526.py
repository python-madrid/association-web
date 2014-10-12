# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0010_auto_20141011_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='summary',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
