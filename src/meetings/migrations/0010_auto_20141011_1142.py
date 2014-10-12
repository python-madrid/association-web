# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0009_auto_20141010_1526'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['title'], 'verbose_name': 'Talk', 'verbose_name_plural': 'Talks'},
        ),
        migrations.RemoveField(
            model_name='talk',
            name='slides',
        ),
        migrations.DeleteModel(
            name='SlideDeck',
        ),
        migrations.AddField(
            model_name='talk',
            name='slide_external',
            field=models.CharField(help_text='Escribe el enlace externo donde esté alojada la presentación', null=True, blank=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talk',
            name='slide_internal',
            field=models.FileField(help_text='Sube aquí la presentación de la charla', null=True, blank=True, upload_to='slides'),
            preserve_default=True,
        ),
    ]
