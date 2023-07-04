from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from .note import Note


class NoteElement(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name=_('note'),
                             help_text=_('The note to which the note element is linked'))
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('name'),
                            help_text=_('Resource title for the administrator purpose of management'))
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('description'),
        help_text=_('Title that can be placed below content on the template to describe content'),)
    text = models.TextField(blank=True, null=True, verbose_name=_('text'),
                            help_text=_('Fill in the field if the note is textual'))
    file = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name=_('file'),
                            help_text=_('Fill in the field if the note is a video'))
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name=_('image'),
                              help_text=_('Fill in the field if the note is an image'))
    order = models.IntegerField(blank=False, verbose_name=_('order'),
                                help_text=_('Order of elements in the note view'))

    def save(self, *args, **kwargs):
        if not any([self.text, self.file, self.image]):
            raise ValidationError(_('Fill one of these field: text, file, image'))
        if sum([bool(self.text), bool(self.file), bool(self.image)]) > 1:
            raise ValidationError(_('Fill only one of these field: text, file, image'))
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
