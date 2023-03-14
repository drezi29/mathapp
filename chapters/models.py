from django.db import models

class Chapter(models.Model):
    name = models.CharField(max_length=128, blank=False)
    lic_class = models.IntegerField(blank=False)
    tech_class = models.IntegerField(blank=False)
    is_extended = models.BooleanField()
    order = models.IntegerField(default=-1, blank=False)
