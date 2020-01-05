from django.urls import path
from _sebelib.templates import register_models, AppHomeResponse
from .views import loginout

## models to register
from .models.client import Client
from .models.staff import Staff
from .models.supplier import Supplier

## register models
API_MODELS_REGITRY = [
    Client, Supplier
]

## accounts/
urlpatterns = [
    ## home
    path('', AppHomeResponse(API_MODELS_REGITRY), name='accounts-home'),

    ## auth
    path('login/',  loginout.login,  name='accounts-login'),
    path('logout/', loginout.logout, name='accounts-logout'),

] + register_models(API_MODELS_REGITRY)

