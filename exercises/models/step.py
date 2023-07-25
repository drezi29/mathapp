from django.db import models
from django.utils.translation import gettext_lazy as _
from .exercise import Exercise


class Step(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name=_('exercise'),
                                 help_text=_('The exercise to which the step is linked'))
    title = models.CharField(max_length=255, verbose_name=_('step title'),
                             help_text=_('Title visible as step title and for administrator purposes'))
    instruction = models.TextField(verbose_name=_('instruction'), help_text=_('Describe the instruction for step'))
    solution = models.TextField(verbose_name=_('instruction'), help_text=_('Solution for step visible as hint'),
                                default=None)
    order = models.IntegerField(blank=False, verbose_name=_('order'),
                                help_text=_('The value determines the order of step in exercise\'s view'))

    def __str__(self):
        return f"{self.title} - Exercise {self.exercise.pk}"

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['exercise', 'order'],
            name='unique_order_for_step_in_exercise')
        ]
        verbose_name = _('step')
        verbose_name_plural = _('steps')
