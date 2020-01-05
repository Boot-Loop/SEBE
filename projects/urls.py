from django.urls import path

#from .views.projects_view import ProjectList, ProjectDetail
from _sebelib.templates import make_list_view_class, make_detail_view_class
from _sebelib.templates import ObjectsResponse

from .models.project import Project

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
   path('list', make_list_view_class(Project).as_view(), name='projects-list'),
   path('<int:pk>/', make_detail_view_class(Project).as_view(), name='project'),
]