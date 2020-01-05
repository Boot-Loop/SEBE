'''
from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.project import Project, ProjectSerializer

from _sebelib.sebedecor import login_required
from _sebelib.templates import (
    list_response_get, detail_response_get, list_response_post, detail_response_put, detail_response_delete
)

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
        return detail_response_get(request, pk, Project, ProjectSerializer)

    @login_required
    def put(self, request, pk, format=None):
        return detail_response_put(request, pk, Project, ProjectSerializer)
    
    @login_required
    def delete(self, request, pk, format=None):
        return detail_response_delete(request, pk, Client)

#'''