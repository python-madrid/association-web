# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255, help_text='Introduce el nombre del autor')),
                ('twitter', models.CharField(null=True, max_length=255, blank=True, help_text='Introduce la cuenta de twitter, por ejemplo: "@python_maddrid"')),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255, help_text='Reunión Python Madrid de Octubre')),
                ('when', models.CharField(max_length=255, help_text='A las 20:30 en las oficinas de Kaleidos')),
                ('venue_link', models.CharField(null=True, max_length=255, blank=True, help_text='Añade aquí un enlace de GMaps por ejemplo')),
                ('summary', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Meetings',
                'verbose_name': 'Meeting',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('internal_file', models.FileField(null=True, upload_to='slides', blank=True, help_text='Sube aquí la presentación de la charla')),
                ('external_file', models.CharField(null=True, max_length=255, blank=True, help_text='Escribe el enlace externo donde esté alojada la presentación')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('video', models.CharField(null=True, max_length=255, blank=True, help_text='Añade aquí el enlace donde esté el vídeo')),
                ('record', models.CharField(null=True, max_length=255, blank=True, help_text='Añade aquí el enlace donde esté el audio')),
                ('author', models.ManyToManyField(to='meetings.Author')),
                ('meeting', models.ForeignKey(to='meetings.Meeting')),
                ('slides', models.ForeignKey(to='meetings.Slide', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Talks',
                'verbose_name': 'Talk',
            },
            bases=(models.Model,),
        ),
    ]
