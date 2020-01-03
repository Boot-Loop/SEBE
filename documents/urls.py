from django.urls import path

from .views.tech_sheet_view import TechnicalSheetList, TechnicalSheetDetail

from .models.technical_sheet import TechnicalSheet

## home page ##################################
from django.shortcuts import reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
from _sebelib.templates import pages_response, ObjectsResponse

@login_required
def home(request): 
    pages = [
        Page('technical-sheets', reverse('documents-technicalsheets'))
    ]
    return pages_response(request, pages, 'Documents')
##################################################

urlpatterns = [
    path('', home, name='documents-home'),

    path('technical-sheets/', ObjectsResponse('Technical Sheets', 'documents-technicalsheets-list', 'documents-technicalsheet', TechnicalSheet), name='documents-technicalsheets'),
    path('technical-sheets/list/', TechnicalSheetList.as_view(), name='documents-technicalsheets-list'),
    path('technical-sheet/<int:pk>/', TechnicalSheetDetail.as_view(), name='documents-technicalsheet'),
]