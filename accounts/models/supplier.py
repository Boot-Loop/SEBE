from django.db import models
from django import forms


class Supplier(models.Model):
    id              = models.IntegerField(primary_key=True)
    company_name    = models.CharField(max_length=50)
    email           = models.EmailField(                null=True, blank=True)
    address         = models.CharField(max_length=100,  null=True, blank=True)

    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'

    def __str__(self):
        return self.company_name
