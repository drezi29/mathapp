from django.contrib import admin
from .models import Chapter

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'lic_class', 'tech_class', 'is_extended', 'order']

admin.site.register(Chapter, ChapterAdmin)