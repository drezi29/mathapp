from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    topic = models.OneToOneField(
        'chapters.Topic',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('topic'),
        help_text=_('The topic to which the quiz is linked'),
    )

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        app_label = 'quiz'

    def __str__(self):
        return f"Quiz: {self.topic}"
