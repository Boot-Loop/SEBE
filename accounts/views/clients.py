from django.shortcuts import render, redirect
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.client import Client, ClientSerializer

from _sebelib.sebedecor import login_required
from _sebelib.templates import (
    list_response_get, list_response_post,
    detail_response_get, get_object, detail_response_post, detail_response_delete
)

class ClientList(APIView):

    @login_required
    def get(self, request):
        return list_response_get(request, Client, ClientSerializer)
    
    @login_required
    def post(self, request):
        return list_response_post(request, ClientSerializer)

class ClientDetail(APIView):

    @login_required
    def get(self, request, pk):
        return detail_response_get(request, pk, Client, ClientSerializer)

    @login_required
    def put(self, request, pk, format=None):
        return detail_response_post(request, pk, Client, ClientSerializer)
    
    @login_required
    def delete(self, request, pk, format=None):
        return detail_response_delete(request, pk, Client)