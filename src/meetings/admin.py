from django.contrib import admin
from .models import (
    Meeting, Talk, Author, SlideDeck
)

class TalkInline(admin.TabularInline):
    model = Talk
    filter_horizontal = ('author',)

class MeetingAdmin(admin.ModelAdmin):
    inlines = [
        TalkInline
    ]

class AuthorAdmin(admin.ModelAdmin):
    pass

class SlideDeckAdmin(admin.ModelAdmin):
    pass

class TalkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(SlideDeck, SlideDeckAdmin)
admin.site.register(Talk, TalkAdmin)