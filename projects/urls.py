from django.urls import path
from _sebelib.templates import register_models, AppHomeResponse

## models to register
from .models.project import Project

## register models
API_MODELS_REGITRY = [
    Project
]

## projects/
urlpatterns = [
   path('', AppHomeResponse(API_MODELS_REGITRY), name='projects-home'),
] + register_models(API_MODELS_REGITRY)
