from django import template

from ..models import FormulaNote

register = template.Library()


@register.filter(name='get_notes_by_title')
def get_notes_by_title(value):
    return FormulaNote.objects.all().filter(title=value)
