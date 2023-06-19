from django.db import models
from .topic import Topic


class Note(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.topic.name} - notatka"
