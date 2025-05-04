from django.db import models
from Movie_Table import Movie_Table
from User_Table import User_Table
import subprocess


class Review_Table(models.Model):
    movie_id = Movie_Table.id
    movie_fmat = Movie_Table.movie_fmat
    user_id = User_Table.id

    feedback = models.CharField(max_length=255)
    rating = models.DecimalField(decimal_places=1,max_digits=2,null=True)
    rate_date = models.DateField(null=True)
