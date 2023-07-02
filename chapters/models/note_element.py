from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from .note import Note


class NoteElement(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name=_('note'))
    name = models.CharField(max_length=128, verbose_name=_('name'))
    description = models.CharField(max_length=255, verbose_name=_('description'))
    text = models.TextField(blank=True, null=True, verbose_name=_('text'))
    file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name=_('file'))
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name=_('image'))
    order = models.IntegerField(blank=False, verbose_name=_('order'))

    def save(self, *args, **kwargs):
        if not any([self.text, self.file, self.image]):
            raise ValidationError('Fill one of these field: text, file, image')
        if sum([bool(self.text), bool(self.file), bool(self.image)]) > 1:
            raise ValidationError('Fill only one of these field: text, file, image')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{str(self.note)} : {self.name}"

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['note', 'order'],
            name='unique_order_for_element_in_note')
        ]
        verbose_name = _('note element')
        verbose_name_plural = _('note elements')
