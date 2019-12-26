from django.urls import path

from .views.projects_view import ProjectView

## home page ##################################
from django.shortcuts import render, reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
@login_required
def home(request):
    pages = []
    return render(request, 'pages.html', {
        'request': request,
        'title'  :'Projects',
        'pages'  : pages
    })
##################################################

urlpatterns = [
   ##path('', home, name='projects-home' ),
   path('', ProjectView.as_view(), name='projects-home'),
]