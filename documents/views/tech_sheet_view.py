from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.technical_sheet import TechnicalSheet, TechnicalSheetSerializer
from _sebelib.sebedecor import login_required
from _sebelib.templates import (
    list_response_get, list_response_post,
    detail_response_get, get_object, detail_response_post, detail_response_delete
)

class TechnicalSheetList(APIView):

    @login_required
    def get(self, request):
        return list_response_get(request, TechnicalSheet, TechnicalSheetSerializer)
    
    @login_required
    def post(self, request, format=None):
        return list_response_post(request, TechnicalSheetSerializer)


class TechnicalSheetDetail(APIView):

    @login_required
    def get(self, request, pk):
        return detail_response_get(request, pk, TechnicalSheet, TechnicalSheetSerializer)

    @login_required
    def put(self, request, pk, format=None):
        return detail_response_post(request, pk, TechnicalSheet, TechnicalSheetSerializer)

    @login_required
    def delete(self, request, pk, format=None):
        return detail_response_delete(request, pk, TechnicalSheet)
