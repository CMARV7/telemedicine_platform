from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    areas_of_specialization = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
