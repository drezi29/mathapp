from django.db import models
from django.utils.translation import gettext_lazy as _

from .title import Title


class FormulaNote(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name=_('title'),
        help_text=_('The chapter of formula card to which the formula note is linked'),
    )
    note = models.TextField(
        verbose_name=_('formula note'),
        help_text=_('Provide note for formula card chapter'),
    )
    order = models.IntegerField(
        blank=False,
        verbose_name=_('order'),
        help_text=_(
            'The value determines the order of notes in formula\'s chapter view'
        ),
    )

    def __str__(self):
        return f'{self.title} - note {self.pk}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'order'], name='unique_order_for_note_in_chapter'
            )
        ]
        verbose_name = _('formula note')
        verbose_name_plural = _('formula notes')
        app_label = 'formula_note'
