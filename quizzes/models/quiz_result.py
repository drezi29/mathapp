from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class QuizResult(models.Model):
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
        verbose_name=_('quiz'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(blank=False)
    answers = (models.TextField(),)
    performing_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Quiz Result')
        verbose_name_plural = _('Quiz Results')
