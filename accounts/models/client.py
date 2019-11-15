from django.db import models
from django import forms

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ## other details

    def __str__(self):
        return self.name