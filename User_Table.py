from django.db import models
import subprocess


class User_Table(models.Model):
    password = models.CharField(max_length=30)

    address = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=100)


