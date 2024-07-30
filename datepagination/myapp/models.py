from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name