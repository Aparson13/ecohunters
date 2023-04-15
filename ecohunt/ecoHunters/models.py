from django.db import models

from django.contrib.auth.models import AbstractUser
from django.views.generic import ListView

class User(AbstractUser):
    name = models.CharField(max_length=70, blank=True, null=True)
    username = models.CharField(max_length=70, blank=True, null=True, unique=True)
    password = models.CharField(max_length=100)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.username

class Leaderboard(ListView):
    model = User
    template_name = 'leaderboard.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.order_by('-score')[:10]





