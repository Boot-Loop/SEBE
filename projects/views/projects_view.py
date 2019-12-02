from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.project import Project, ProjectSerializer

class ProjectView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('accounts-login')

        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        