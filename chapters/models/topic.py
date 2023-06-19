from django.db import models
from .chapter import Chapter


class Topic(models.Model):
    name = models.CharField(max_length=128, blank=False)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    is_extended = models.BooleanField()
    order = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.name} - {str(self.chapter.name)}"

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['chapter', 'order'],
            name='unique_order_for_topics_in_chapter')
        ]
