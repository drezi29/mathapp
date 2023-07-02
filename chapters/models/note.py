from django.db import models
from django.utils.translation import gettext_lazy as _
from .topic import Topic


class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=_('topic'))

    def __str__(self):
        return f"{self.topic.name} - notatka"

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')