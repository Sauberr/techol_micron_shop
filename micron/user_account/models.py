from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.utils import timezone


class User(AbstractUser):
    image = models.ImageField(upload_to='avatar', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)



