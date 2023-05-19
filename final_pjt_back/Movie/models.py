from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=100,null=True)
    original_title = models.CharField(max_length=100, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    overview = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    genres = models.ManyToManyField(Genre, blank=True)


# class Review(models.Model):
#     content = models.CharField(max_length=100)
#     rank = 

