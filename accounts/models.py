from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser (AbstractUser):
    place = models.CharField(max_length=50, null=True, blank=True, default="place")
