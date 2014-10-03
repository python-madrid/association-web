# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_meeting_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, default='', blank=True),
            preserve_default=False,
        ),
    ]
