from django.urls import path
from drfvg import register_models

## view functions
from .views import loginout

## models to register
from .models.client import Client
from .models.staff import Staff
from .models.supplier import Supplier

## accounts/
urlpatterns = [

    path('login/',  loginout.login,  name='accounts-login'),
    path('logout/', loginout.logout, name='accounts-logout'),

] + register_models( [ Client, Supplier ], app_name='accounts') 
