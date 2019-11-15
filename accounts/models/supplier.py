from django.db import models
from django import forms

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    ## other details

    def __str__(self):
        return self.name