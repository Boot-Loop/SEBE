from django.db import models
from django import forms

from rest_framework import serializers

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    ## other details

    def __str__(self):
        return self.name

    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Client
        fields = [ 'name', 'email' ]