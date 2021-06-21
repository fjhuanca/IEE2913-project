from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_medic = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)