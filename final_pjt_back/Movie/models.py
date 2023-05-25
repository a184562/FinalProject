from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# 영화 장르 데이터 모델
class Genre(models.Model):
    name = models.TextField()

# 영화 데이터 모델
class Movie(models.Model):
    title = models.CharField(max_length=100,null=True)
    original_title = models.CharField(max_length=100, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    overview = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

# 한줄평 데이터 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="moviecomments")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
