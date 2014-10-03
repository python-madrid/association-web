# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0005_auto_20141003_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
    ]
