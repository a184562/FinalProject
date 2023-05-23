from django.db import models
from django.contrib.auth.models import AbstractUser

class Genre(models.Model):
    name = models.TextField()

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)