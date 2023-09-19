import nested_admin
from django.contrib import admin

from .models import FormulaNote, Title

admin.site.register(FormulaNote)


class FormulaNoteInline(nested_admin.NestedStackedInline):
    model = FormulaNote
    sortable_field_name = 'title'


class TitleAdmin(nested_admin.NestedModelAdmin):
    inlines = [FormulaNoteInline]


admin.site.register(Title, TitleAdmin)
