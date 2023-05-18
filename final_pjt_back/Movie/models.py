from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=100,unique=True)
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    popularity = models.FloatField()
    genres = models.ManyToManyField(Genre)


