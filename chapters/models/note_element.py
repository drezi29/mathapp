from django.core.exceptions import ValidationError
from django.db import models
from .note import Note


class NoteElement(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    order = models.IntegerField(blank=False)

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
