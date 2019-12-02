from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.client import Client, ClientSerializer
from ..models.supplier import Supplier, SupplierSerializer

class ClientView(APIView):

    def get(self, request):
        if not request.user.is_authenticated: return redirect('accounts-login')

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        if not request.user.is_authenticated: return redirect('accounts-login')

        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierView(APIView):

    def get(self, request):
        if not request.user.is_authenticated: return redirect('accounts-login')

        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    