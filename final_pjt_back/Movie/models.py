from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    popularity = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    runtime = models.IntegerField()

class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_moviecomments')
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
