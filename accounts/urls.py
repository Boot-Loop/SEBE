from django.urls import path, include
from .views import auth_view

urlpatterns = [
    path('login/', auth_view.login, name='accounts-login'),
    path('logout/', auth_view.logout, name='accounts-logout' ),
    path('register/', auth_view.register, name='accounts-register' ), ## for superuser
    
    path('forgot-password/', auth_view.forgot_password, name='accounts-forgot_password'),
]