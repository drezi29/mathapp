from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    chapter = models.OneToOneField('chapters.Chapter', on_delete=models.SET_NULL, null=True, verbose_name=_('chapter'))

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.chapter.name


class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, verbose_name=_('quiz'))
    question_content = models.TextField(verbose_name=_('question content'))

    def __str__(self):
        return self.question_content

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name=_('question'))
    answer_content = models.CharField(max_length=255, verbose_name=_('answer content'))
    is_correct = models.BooleanField(default=False, verbose_name=_('is correct'))

    def check_correctness(self, user_answer) -> bool:
        return self.is_correct == user_answer

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answer')
