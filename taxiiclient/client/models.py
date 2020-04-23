from django.db import models

# Create your models here.

class Indicator(models.Model):
    type = models.CharField(max_length=50)
    id = models.CharField(max_length=50, primary_key=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    name = models.CharField(max_length=50)
    pattern = models.CharField(max_length=100)
    valid_from = models.DateTimeField()
    labels = models.CharField(max_length=500)

    def __str__(self):
        return self.name

