# booking/models.py
from django.db import models

class Machinery(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


