from django.urls import path, include
from .views import loginout

from .views.clients import ClientView
from .views.suppliers import SupplierView

## home page ##################################
from django.shortcuts import render, reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
@login_required
def home(request):
    pages = []
    return render(request, 'pages.html', {
        'request': request,
        'title'  : 'Accounts',
        'pages'  : pages
    })
##################################################

## accounts/
urlpatterns = [
    ## home
    path('', home, name='accounts-home'),

    ## auth
    path('login/',  loginout.login,  name='accounts-login'),
    path('logout/', loginout.logout, name='accounts-logout'),

    ## api view
    path('clients/',   ClientView.as_view(),   name='accounts-client'),
    path('suppliers/', SupplierView.as_view(), name='accounts-suppliers'),
]
