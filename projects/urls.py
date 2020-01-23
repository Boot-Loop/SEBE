from django.urls import path
from drfvg import register_models

## models to register
from .models.project import Project

## projects/
urlpatterns = [ ] + register_models( [ Project ], app_name='projects')

