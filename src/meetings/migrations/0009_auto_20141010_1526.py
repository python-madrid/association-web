# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_auto_20141003_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='when_where',
        ),
        migrations.AddField(
            model_name='meeting',
            name='when',
            field=models.CharField(null=True, blank=True, help_text='23 de septiembre de 2014, a partir de las 20:30', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meeting',
            name='where',
            field=models.CharField(null=True, blank=True, help_text='Oficinas de Kaleidos. Calle La Botánica, 4', max_length=255),
            preserve_default=True,
        ),
    ]
