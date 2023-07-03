from django.db import models
from django.utils.translation import gettext_lazy as _


class Note(models.Model):
    topic = models.ForeignKey('chapters.Topic', on_delete=models.CASCADE, verbose_name=_('topic'),
                              help_text=_('The topic to which the note is linked'))

    def __str__(self):
        return f"{self.topic.name}: note"

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')
