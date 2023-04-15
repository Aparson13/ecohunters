from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=70, blank=True, null=True)
    username = models.CharField(max_length=70, blank=True, null=True, unique=True)


