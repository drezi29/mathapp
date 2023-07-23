from django.db import models
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):
    topic = models.ForeignKey('chapters.Topic', on_delete=models.CASCADE, verbose_name=_('topic'),
                              help_text=_('The topic to which the exercise is linked'))
    exercise_content = models.TextField(verbose_name=_('exercise content'),
                                        help_text=_('Describe the content of exercise - the command'))
    title = models.CharField(max_length=255, verbose_name=_('exercise title'),
                             help_text=_('Title visible as exercise title in exercises list'))
    is_extended = models.BooleanField(verbose_name=_('is extended'),
                                      help_text=_('Should be checked if exercise belongs to the extended level'))

    def __str__(self):
        return f"{self.title}: {self.topic.name}"

    class Meta:
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')
