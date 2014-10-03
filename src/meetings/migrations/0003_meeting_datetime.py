# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20141001_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
