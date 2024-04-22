from django import template

from ..models import Answer

register = template.Library()


@register.filter(name='get_correct_answer')
def get_correct_answer(question_id):
    return Answer.objects.get(question=question_id, is_correct=True).answer_content
