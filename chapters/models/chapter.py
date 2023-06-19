from django.db import models


class Chapter(models.Model):
    name = models.CharField(max_length=128, blank=False)
    program_class = models.IntegerField(blank=False, verbose_name='class')
    is_extended = models.BooleanField()
    order = models.IntegerField(blank=False, unique=True)

    def __str__(self):
        return f"{self.name} - klasa {str(self.program_class)}"
    
    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['program_class', 'order'],
            name='unique_order_for_chapters_for_each_class')
        ]
