from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.project import Project, ProjectSerializer

from _sebelib.sebedecor import login_required
from _sebelib.templates import list_response_get, detail_response, list_response_post

class ProjectList(APIView):

    @login_required
    def get(self, request):
        return list_response_get(request, Project, ProjectSerializer)
    
    @login_required
    def post(self, request):
        return list_response_post(request, ProjectSerializer)


class ProjectDetail(APIView):

    @login_required
    def get(self, request, pk):
        return detail_response(request, pk, Project, ProjectSerializer)
