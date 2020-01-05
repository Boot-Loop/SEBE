from django.db import models
from django import forms


class Client(models.Model):

    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=20)
    email           = models.EmailField()
    address         = models.CharField(max_length=100)
    ## other details 

    def __str__(self):
        return self.first_name

#from rest_framework import serializers
'''
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Client
        fields = [ 'id', 'first_name', 'last_name', 'phone_number', 'email', 'address' ]
    
    ##def create(self, validated_data):
    ##    profile_data = validated_data.pop('profile')
    ##    user = User.objects.create(**validated_data)
    ##    Profile.objects.create(user=user, **profile_data)
    ##    return user
    
    ##def update(self, instance, validated_data):
    ##    instance.first_name      = validated_data.get('first_name',     instance.first_name  )
    ##    instance.last_name       = validated_data.get('last_name',      instance.last_name   )
    ##    instance.phone_number    = validated_data.get('phone_number',   instance.phone_number)
    ##    instance.email           = validated_data.get('email',          instance.email       )
    ##    instance.address         = validated_data.get('address',        instance.address     )
    ##    
    ##    instance.save()
    ##    return instance




#'''