from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
