from django.contrib import admin
from .models import (
    Meeting, Talk, Author, Slide
)

class TalkInline(admin.TabularInline):
    model = Talk

class MeetingAdmin(admin.ModelAdmin):
    inlines = [
        TalkInline
    ]

class AuthorAdmin(admin.ModelAdmin):
    pass

class SlideAdmin(admin.ModelAdmin):
    pass

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Slide, SlideAdmin)
