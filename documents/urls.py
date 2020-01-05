from django.urls import path
from _sebelib.templates import register_models, AppHomeResponse

## models to register
from .models.technical_sheet import TechnicalSheet

## register models
API_MODELS_REGITRY = [
    TechnicalSheet
]

## documents/
urlpatterns = [
    path('', AppHomeResponse(API_MODELS_REGITRY), name='documents-home'),
] + register_models(API_MODELS_REGITRY)




