__author__ = 'sachin yadav'

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True,on_delete="CASECADE")
