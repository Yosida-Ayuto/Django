from tabnanny import verbose
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'