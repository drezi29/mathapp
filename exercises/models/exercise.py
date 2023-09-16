from django.db import models
from django.utils.translation import gettext_lazy as _


class Exercise(models.Model):
    topic = models.ForeignKey(
        'chapters.Topic',
        on_delete=models.CASCADE,
        verbose_name=_('topic'),
        help_text=_('The topic to which the exercise is linked'),
    )
    exercise_content = models.TextField(
        verbose_name=_('exercise content'),
        help_text=_('Describe the content of exercise - the command'),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_('exercise title'),
        help_text=_('Title visible as exercise title in exercises list'),
    )
    is_extended = models.BooleanField(
        verbose_name=_('is extended'),
        help_text=_('Should be checked if exercise belongs to the extended level'),
    )
    order = models.IntegerField(
        blank=False,
        unique=True,
        default=0,
        verbose_name=_('order'),
        help_text=_(
            'The value determines the order of exercise in exercises\' list view'
        ),
    )

    def __str__(self):
        return f'{self.title}: {self.topic.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['topic', 'order'], name='unique_order_for_exercise_in_topic'
            )
        ]
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')
