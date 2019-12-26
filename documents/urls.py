from django.urls import path

from .views.tech_sheet_view import TechnicalSheetView

## home page ##################################
from django.shortcuts import render, reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
@login_required
def home(request):
    pages = []
    return render(request, 'pages.html', {
        'request': request,
        'title'  : 'Documetns',
        'pages'  : pages
    })
##################################################

urlpatterns = [
    path('', home, name='documents-home'),

    path('technical-sheets/', TechnicalSheetView.as_view(), name='documents-technicalsheet'),
]