from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length =20)
    email = models.EmailField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name


