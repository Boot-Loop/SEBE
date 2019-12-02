from django.urls import path

from .views.tech_sheet_view import TechnicalSheetView

urlpatterns = [
    path('technical-sheets/', TechnicalSheetView.as_view(), name='documents-technicalsheet'),
]