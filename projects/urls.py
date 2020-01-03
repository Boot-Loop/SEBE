from django.urls import path

from .views.projects_view import ProjectList, ProjectDetail
from .models.project import Project


from _sebelib.templates import ObjectsResponse

## home page ##################################
## from django.shortcuts import reverse
## from _sebelib import Page
## from _sebelib.sebedecor import login_required
## from _sebelib.templates import pages_response, ObjectsResponse
## 
## 
## @login_required
## def home(request): 
##     pages = []
##     return pages_response(request, pages, 'Projects')
##################################################

urlpatterns = [
   path('', ObjectsResponse('Projects', 'projects-list', 'project', Project ), name='projects'),
   path('list', ProjectList.as_view(), name='projects-list'),
   path('<int:pk>/', ProjectDetail.as_view(), name='project'),
]