from django.urls import path, include
from .views import loginout
from django.http import JsonResponse

from _sebelib.templates import make_detail_view_class, make_list_view_class
#from .views.clients import ClientList, ClientDetail
#from .views.suppliers import SupplierList, SupplierDetail

from .models.client import Client
from .models.staff import Staff
from .models.supplier import Supplier

## home page ##################################
from django.shortcuts import reverse
from _sebelib import Page
from _sebelib.sebedecor import login_required
from _sebelib.templates import pages_response, ObjectsResponse

@login_required
def home(request): 
    pages = [
        Page('clients', reverse('accounts-clients')),
        Page('suppliers', reverse('accounts-suppliers')),
    ]
    return pages_response(request, pages, 'Accounts')
    
##################################################

## accounts/
urlpatterns = [
    ## home
    path('', home, name='accounts-home'),

    ## auth
    path('login/',  loginout.login,  name='accounts-login'),
    path('logout/', loginout.logout, name='accounts-logout'),

    ## api view
    path('clients/',            ObjectsResponse('Clients', 'accounts-clients-list', 'account-client', Client),   name='accounts-clients'),
    path('clients/list/',       make_list_view_class(Client).as_view(),   name='accounts-clients-list'),
    path('client/<int:pk>/',    make_detail_view_class(Client).as_view(), name='account-client'),

    path('suppliers/',          ObjectsResponse('Suppliers', 'accounts-suppliers-list', 'accounts-supplyer', Supplier), name='accounts-suppliers'),
    path('suppliers/list/',     make_list_view_class(Supplier).as_view(), name='accounts-suppliers-list'),
    path('supplier/<int:pk>/',  make_detail_view_class(Supplier).as_view(), name='accounts-supplyer'),
]
