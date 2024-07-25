from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    GEEKS_CHOICES =(  
    ("1", "Employee"),  
    ("2", "Manager"),) 
    userchoice = models.CharField(max_length=1,choices = GEEKS_CHOICES)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    
class NewUserModel(models.Model):
    # id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    GEEKS_CHOICES =(  
    ("1", "Employee"),  
    ("2", "Manager"),)
    userchoice = models.CharField(max_length=1,choices = GEEKS_CHOICES)

    def __str__(self):
        return self.username

