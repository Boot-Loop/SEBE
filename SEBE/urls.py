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


## home page ##################################
from django.shortcuts import render, reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
@login_required
def home(request):
    return render(request, 'pages.html', context={
        'request':request,
        'title'  : 'SEBE',
        'pages':[
            Page('accounts', reverse('accounts-home')),
            Page('documents', reverse('documents-home')),
            Page('projects', reverse('projects-home')),
        ]
    })
##################################################

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home, name='home-page'),

    path('accounts/',  include('accounts.urls' )),
    path('projects/',  include('projects.urls')),
    path('documents/', include('documents.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT_PUBLIC)
