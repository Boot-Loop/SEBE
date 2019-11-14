from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate

from ..models.staff import LoginForm
from SEBE.core.apidata_template import ApiDataTemplate
from SEBE.core.sebe_response import SEBEResponse

def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return SEBEResponse.create_response(
                    request,
                    api_data=ApiDataTemplate('Login success'), 
                    status_code=200,
                    is_redirect=True, redirect_to='home-page'
                )

            else:
                return SEBEResponse.create_response(
                    request, 
                    api_data = ApiDataTemplate('Authentication Error: user not exists', ApiDataTemplate.STATUS_ERROR).as_dict(), 
                    status_code=404,
                    message=messages.error(request, f'Authentication failed. (check your username and password)'), 
                    is_redirect=True, redirect_to='accounts-login'
                )

    else:
        messages.error(request,'Error: invalid login form')
        return redirect('accounts-login')