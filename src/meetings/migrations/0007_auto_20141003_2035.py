# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_auto_20141003_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='when_where',
            field=models.CharField(help_text='A las 20:30 en las oficinas de Kaleidos', null=True, blank=True, max_length=255),
        ),
    ]
