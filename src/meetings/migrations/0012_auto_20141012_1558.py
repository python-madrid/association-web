# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0011_auto_20141012_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='record',
        ),
        migrations.RemoveField(
            model_name='talk',
            name='slide_external',
        ),
        migrations.RemoveField(
            model_name='talk',
            name='video',
        ),
    ]
