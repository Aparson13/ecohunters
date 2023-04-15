from django.db import models

# Create your models here.

# Create your models here.
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib import admin
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.contrib.auth.models import AbstractUser #add this
from django.db.models import Avg, Count
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        username=username,
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self,username, email, password, **extra_fields):
    return self._create_user(username, email, password, False, False, **extra_fields)

  def create_superuser(self, username, email, password, **extra_fields):
    user=self._create_user(username, email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user

class User(AbstractUser):
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    # is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [ 'email']

    # objects = UserManager()
    

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

# Add Location (as multiple choice and make a default rating
    def __str__(self):
        return self.year

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name', 'email']