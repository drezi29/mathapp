from django.db import models
from django.utils.translation import gettext_lazy as _


class Chapter(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name=_('name'))
    program_class = models.IntegerField(blank=False, verbose_name=_('class'))
    is_extended = models.BooleanField(verbose_name=_('is extended'),
                                      help_text=_('Should be checked if chapter belongs to the extended level'))
    order = models.IntegerField(blank=False, unique=True, verbose_name=_('order'),
                                help_text=_('The value determines the order of chapters in table of content'))

    def __str__(self):
        return f"{self.name}: {str(self.program_class)}"
    
    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['program_class', 'order'],
            name='unique_order_for_chapters_for_each_class')
        ]
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')
