from django import forms
import nested_admin
from django.contrib import admin
from .models import NoteElement, Note


class NoteElementAdmin(admin.ModelAdmin):
    list_display = ['note', 'name', 'order']


admin.site.register(NoteElement, NoteElementAdmin)


class NoteElementInline(nested_admin.NestedStackedInline):
    model = NoteElement
    sortable_field_name = "name"


class NoteAdmin(nested_admin.NestedModelAdmin):
    inlines = [NoteElementInline]

admin.site.register(Note, NoteAdmin)
