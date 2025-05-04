from django.db import models
import subprocess


class Movie_Table(models.Model):
    movie_fmat = models.CharField(max_length=3)

    storage_link = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    release_date = models.DateField(null=True)


