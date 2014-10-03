# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0007_auto_20141003_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='summary',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
