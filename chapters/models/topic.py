from django.db import models
from django.utils.translation import gettext_lazy as _
from .chapter import Chapter


class Topic(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name=_('name'))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('chapter'),
                                help_text=_('The chapter to which the topic is linked'))
    is_extended = models.BooleanField(verbose_name=_('is extended'),
                                      help_text=_('Should be checked if chapter belongs to the extended level'))
    order = models.IntegerField(blank=False, verbose_name=_('order'),
                                help_text=_('The value determines the order of topics in chapter\'s table of content'))

    def __str__(self):
        return f"{self.name} - {str(self.chapter.name)}"

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['chapter', 'order'],
            name='unique_order_for_topics_in_chapter')
        ]
        verbose_name = _('topic')
        verbose_name_plural = _('topics')