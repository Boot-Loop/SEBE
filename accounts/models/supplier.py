from django.db import models
from django import forms


class Supplier(models.Model):
    class Meta:
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'

    company_name = models.CharField(max_length=50)
    email        = models.EmailField()
    address      = models.CharField(max_length=100)

    ## other details

    def __str__(self):
        return self.company_name
