from django.db import models
from django.contrib.auth.models import AbstractUser

# 장르 모델(id, name)
class Genre(models.Model):
    name = models.TextField()

# 유저 모델(기본 AbstractUser 모델 + a)
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)