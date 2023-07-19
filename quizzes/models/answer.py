from django.db import models
from django.utils.translation import gettext_lazy as _
from .question import Question


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name=_('question'),
                                 help_text=_('The question to which the answer is linked'))
    answer_content = models.CharField(max_length=255, verbose_name=_('answer content'))
    is_correct = models.BooleanField(default=False, verbose_name=_('is correct'),
                                     help_text=_('Should be checked if the answer is correct for the question'))

    def check_correctness(self, user_answer) -> bool:
        return self.is_correct == user_answer

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answer')
