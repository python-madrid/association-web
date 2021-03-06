from django.db import models
from ckeditor.fields import RichTextField

class Meeting(models.Model):
    title = models.CharField(max_length=255,
        blank=False, null=False,
        help_text='Reunión Python Madrid de Octubre'
    )
    slug  = models.SlugField(max_length=255,
        blank=True, null=False,
        unique=True, db_index=True, editable=True
    )
    when = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='23 de septiembre de 2014, a partir de las 20:30'
    )
    where = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Oficinas de Kaleidos. Calle La Botánica, 4'
    )
    datetime = models.DateTimeField(
        blank=True, null=True
    )
    venue_link = models.CharField(max_length=255,
        blank=True, null=True,
        help_text='Añade aquí un enlace de GMaps por ejemplo'
    )
    summary = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'


class Talk(models.Model):
    meeting = models.ForeignKey('Meeting',
        blank=False, null=False,
        related_name='talks'
    )
    title = models.CharField(max_length=255,
        blank=False, null=False
    )
    authors = models.ManyToManyField('Author',
        related_name='authors'
    )
    summary = RichTextField(blank=True, null=True)
    slide_internal = models.FileField(
        blank=True, null=True, upload_to='slides',
        help_text='Sube aquí la presentación de la charla'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Talk'
        verbose_name_plural = 'Talks'
        ordering = ['title']


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
