"""SEBE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

## must match the app name and must have urls.py
HOME_PAGE_APPS_REGISTRY = [
    'accounts',
    'documents',
    'projects',
]

## home page ##################################
from django.shortcuts import render, reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
from _sebelib.templates import pages_response
@login_required
def home(request):
    pages = []
    for app_name in HOME_PAGE_APPS_REGISTRY:
        pages.append(Page(app_name, reverse('%s-home'%app_name)))
    return pages_response(request, pages, 'SEBE')

from django.http import JsonResponse
def test():
    return JsonResponse({'message':'test'})
##################################################

admin.site.site_header = "SEBE Admin"
admin.site.site_title = "SEBE"
admin.site.index_title = "wellcome to SEBE"

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name='home-page'),
    path('test/', test), ## for testing
]
## register apps urls
for app_name in HOME_PAGE_APPS_REGISTRY:
    urlpatterns.append(path( '%s/'%app_name, include('%s.urls'%app_name) ))

