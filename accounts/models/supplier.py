from django.db import models
from django import forms

from rest_framework import serializers

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    ## other details

    def __str__(self):
        return self.name

    
## serializers
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Supplier
        fields = [ 'name' ]
