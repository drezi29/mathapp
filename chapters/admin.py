from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Chapter, Topic


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_class', 'is_extended', 'order']


admin.site.register(Chapter, ChapterAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'chapter', 'is_extended', 'order']


admin.site.register(Topic, TopicAdmin)
