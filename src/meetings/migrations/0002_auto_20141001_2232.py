# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Slide',
            new_name='SlideDeck',
        ),
        migrations.RenameField(
            model_name='meeting',
            old_name='when',
            new_name='when_where',
        ),
    ]
