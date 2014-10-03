# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_meeting_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='author',
        ),
        migrations.AddField(
            model_name='talk',
            name='authors',
            field=models.ManyToManyField(related_name='authors', to='meetings.Author'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='talk',
            name='meeting',
            field=models.ForeignKey(related_name='talks', to='meetings.Meeting'),
        ),
    ]
