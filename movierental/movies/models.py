from django.db import models

class Movie_Table(models.Model):
    movie_fmat = models.CharField(max_length=3)

    storage_link = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    release_date = models.DateField(null=True)
class User_Table(models.Model):
    password = models.CharField(max_length=30)

    address = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
class Review_Table(models.Model):
    movie_id = Movie_Table.id
    movie_fmat = Movie_Table.movie_fmat
    user_id = User_Table.id

    feedback = models.CharField(max_length=255)
    rating = models.DecimalField(decimal_places=1,max_digits=2,null=True)
    rate_date = models.DateField(null=True)
