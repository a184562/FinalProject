from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class MovieLikes(AbstractUser):
    movielike = models.ManyToManyField('self', symmetrical=False, related_name='movielike')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    genres = models.IntegerField()
    release_date = models.DateField()
    popularity = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    Likes = models.ForeignKey(MovieLikes, on_delete=models.CASCADE)


