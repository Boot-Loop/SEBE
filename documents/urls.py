from django.urls import path
from drfvg import register_models

## models to register
from .models.technical_sheet import TechnicalSheet

## documents/
urlpatterns = [ ] + register_models( [ TechnicalSheet ], app_name='documents')




