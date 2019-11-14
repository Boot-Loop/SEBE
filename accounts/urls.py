from django.urls import path

from .views import auth_view

urlpatterns = [
    path('login/',  auth_view.login,  name='accounts-login'),
    path('logout/', auth_view.logout, name='accounts-logout' ),
]