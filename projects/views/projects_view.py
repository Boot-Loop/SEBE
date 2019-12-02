from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.project import Project, ProjectSerializer

class ProjectView(APIView):

    def get(self, request):
        if not request.user.is_authenticated: return redirect('accounts-login')

        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_authenticated: return redirect('accounts-login')

        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
