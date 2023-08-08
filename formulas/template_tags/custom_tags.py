from django import template
from ..models import FormulaNote


register = template.Library()


@register.filter(name='get_notes')
def get_notes(value):
    return FormulaNote.objects.all().filter(title=value)
