from django.urls import path

from .views.projects_view import ProjectView

urlpatterns = [
   path('', ProjectView.as_view(), name='projects'),
]