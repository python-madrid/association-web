from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=255,
        blank=False, null=False,
        help_text='Reunión Python Madrid de Octubre'
    )
    when_where = models.CharField(max_length=255,
        blank=False, null=False,
        help_text='A las 20:30 en las oficinas de Kaleidos'
    )
    datetime = models.DateTimeField(
        blank=True, null=True
    )
    venue_link = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Añade aquí un enlace de GMaps por ejemplo'
    )
    summary = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'


class Talk(models.Model):
    meeting = models.ForeignKey('Meeting',
        blank=False, null=False
    )
    title = models.CharField(max_length=255,
        blank=False, null=False
    )
    author = models.ManyToManyField('Author')
    summary = models.TextField()
    slides = models.ForeignKey('SlideDeck',
        blank=True, null=True
    )
    video = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Añade aquí el enlace donde esté el vídeo'
    )
    record = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Añade aquí el enlace donde esté el audio'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Talk'
        verbose_name_plural = 'Talks'


class Author(models.Model):
    name = models.CharField(max_length=255,
        blank=False, null=False,
        help_text='Introduce el nombre del autor'
    )
    twitter = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Introduce la cuenta de twitter, por ejemplo: "@python_maddrid"'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

class SlideDeck(models.Model):
    internal_file = models.FileField(
        blank=True, null=True, upload_to='slides',
        help_text='Sube aquí la presentación de la charla'
    )
    external_file = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Escribe el enlace externo donde esté alojada la presentación'
    )
