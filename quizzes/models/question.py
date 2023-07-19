from django.db import models
from django.utils.translation import gettext_lazy as _
from .quiz import Quiz


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, verbose_name=_('quiz'),
                             help_text=_('The quiz to which the question is linked'))
    question_content = models.TextField(verbose_name=_('question content'))

    def __str__(self):
        return f"{self.question_content}: {self.quiz}"

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
