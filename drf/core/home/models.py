from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# class CustomUser(AbstractUser):

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=False, blank=False, default=0)  

    def __str__(self):
        return f"{self.user.username}'s Profile"








# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


    


