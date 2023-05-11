from django import forms
import nested_admin
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Chapter, NoteElement, Note, Topic 


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_class', 'is_extended', 'order']


admin.site.register(Chapter, ChapterAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'chapter', 'is_extended', 'order']


admin.site.register(Topic, TopicAdmin)


class NoteElementAdmin(admin.ModelAdmin):
    list_display = ['note', 'name', 'order']


admin.site.register(NoteElement, NoteElementAdmin)


class NoteElementInline(nested_admin.NestedStackedInline):
    model = NoteElement
    sortable_field_name = "name"


class NoteAdmin(nested_admin.NestedModelAdmin):
    inlines = [NoteElementInline]

admin.site.register(Note, NoteAdmin)