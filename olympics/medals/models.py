from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    gold = models.PositiveIntegerField(default=0)
    silver = models.PositiveIntegerField(default=0)
    bronze = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.country
    