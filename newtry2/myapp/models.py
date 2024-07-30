# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.
# class CustomUser(AbstractUser):
#     USER_TYPE_CHOICES = (
#         (1, 'manager'),
#         (2, 'employee'),
#     )

#     usermodel = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    
#     def __str__(self):
#         usermodel = "admin"
#         for user in self.USER_TYPE_CHOICES:
#             if user[0] == self.usermodel:
#                 usermodel = user[1]
#                 break
#         return "{} : {}".format(self.username, usermodel)


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    USER_TYPE_CHOICES = (
        (1, 'manager'),
        (2, 'employee'),
    )

    usermodel = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)
    
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
