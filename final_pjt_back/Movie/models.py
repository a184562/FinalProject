from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    popularity = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    runtime = models.IntegerField()
    

