from django.urls import path, include
from .views import auth_view

from .views.api_views import ClientView, SupplierView

## accounts/
urlpatterns = [
    path('login/', auth_view.login, name='accounts-login'),
    path('logout/', auth_view.logout, name='accounts-logout' ),
    path('register/', auth_view.register, name='accounts-register' ), ## for superuser
    path('forgot-password/', auth_view.forgot_password, name='accounts-forgot_password'),

    ## api view
    path( 'clients/', ClientView.as_view(), name='accounts-client' ),
    path('suppliers/', SupplierView.as_view(), name='accounts-suppliers'),

]
