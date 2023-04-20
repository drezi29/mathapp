from django.db import models
from django.core.exceptions import ValidationError

class Chapter(models.Model):
    name = models.CharField(max_length=128, blank=False)
    program_class = models.IntegerField(blank=False, verbose_name='class')
    is_extended = models.BooleanField()
    order = models.IntegerField(blank=False, unique=True)

    def __str__(self):
        return (self.name + ' - klasa ' + str(self.program_class))
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['program_class', 'order'], name='unique_order_for_chapters_for_each_class')]

class Topic(models.Model):
    name = models.CharField(max_length=128, blank=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    is_extended = models.BooleanField()
    order = models.IntegerField(blank=False)

    def __str__(self):
            return (self.name + ' - ' + str(self.chapter.name))
    
    class Meta:
        constraints = [models.UniqueConstraint(fields=['chapter', 'order'], name='unique_order_for_topics_in_chapter')]

class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return 'Notatka ' + self.topic.name

class NoteElement(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to ='uploads/', blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    order = models.IntegerField(blank=False)

    def save(self, *args, **kwargs):
        if not self.text and not self.file and not self.image:
            raise ValidationError('Fill one of these field: text, file, image')
        if (self.text and (self.file or self.image)) or (self.file and (self.text or self.image)) or (self.image and (self.text or self.file)):
             raise ValidationError('Fill only one of these field: text, file, image')
        super().save(*args, **kwargs)

    def __str__(self):
            return str(self.note) + ': ' + self.name

    class Meta:
        constraints = [models.UniqueConstraint(fields=['note', 'order'], name='unique_order_for_element_in_note')]