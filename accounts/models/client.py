from django.db import models
from django import forms


class Client(models.Model):
    id              = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=40, null=True, blank=True)
    address         = models.CharField(max_length=50, null=True, blank=True)
    email           = models.EmailField(              null=True, blank=True)
    company         = models.CharField(max_length=40, null=True, blank=True)
    position        = models.CharField(max_length=40, null=True, blank=True)
    nic             = models.CharField(max_length=10, null=True, blank=True)
    telephone       = models.CharField(max_length=20, null=True, blank=True)
    website         = models.CharField(max_length=40, null=True, blank=True)
    comments        = models.TextField(               null=True, blank=True)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.name