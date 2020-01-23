from django.urls import path
from drfvg import register_models

## models to register
from .models.client import Client
from .models.staff import Staff
from .models.supplier import Supplier

## accounts/
urlpatterns = [ ] + register_models( [ Client, Supplier ], app_name='accounts') 
