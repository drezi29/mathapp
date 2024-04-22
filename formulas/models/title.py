from django.db import models
from django.utils.translation import gettext_lazy as _


class Title(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_('formulas\' scope title'),
        help_text=_('Title visible as chapter in formula\'s card'),
    )
    order = models.IntegerField(
        blank=False,
        verbose_name=_('order'),
        unique=True,
        help_text=_(
            'The value determines the order of chapters in formulas\'s card view'
        ),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('title')
        verbose_name_plural = _('titles')
        app_label = 'title'
