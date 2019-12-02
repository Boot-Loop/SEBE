from django.db import models
from django import forms

from rest_framework import serializers

class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    email        = models.EmailField()
    address      = models.CharField(max_length=100)

    ## other details

    def __str__(self):
        return self.company_name

    
## serializers
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Supplier
        fields = [ 'id', 'company_name', 'email', 'address' ]
