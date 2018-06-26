from django.db import models

# Create your models here.
class Users(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    def __str__(self):
        return self.Name

