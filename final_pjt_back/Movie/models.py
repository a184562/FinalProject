from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    genres = models.IntegerField()
    release_date = models.DateField()
    popularity = models.IntegerField()
    genres = models.ManyToManyField(Genre)


    