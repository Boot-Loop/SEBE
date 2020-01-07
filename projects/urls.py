from django.urls import path
from _sebelib.templates import register_models, AppHomeResponse

## models to register
from .models.project import Project

## register models
API_MODELS_REGITRY = [
    Project
]
APP_NAME = 'projects'

## projects/
urlpatterns = [
   path('', AppHomeResponse(API_MODELS_REGITRY), name='%s-home'%APP_NAME),
] + register_models(API_MODELS_REGITRY)
