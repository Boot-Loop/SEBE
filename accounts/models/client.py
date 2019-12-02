from django.db import models
from django import forms

from rest_framework import serializers

class Client(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=20)
    email           = models.EmailField()
    address         = models.CharField(max_length=100)
    ## other details 

    def __str__(self):
        return self.first_name

    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Client
        fields = [ 'first_name', 'last_name', 'phone_number', 'email', 'address' ]
