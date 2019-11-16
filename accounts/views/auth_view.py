from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import auth

from ..controls import auth_ctrl
from ..models.staff import LoginForm, StaffCreationForm

from SEBE.core.form_template import SEBEFormTemplate
from SEBE.core.context import FormContext
from SEBE.core.sebe_response import SEBEResponse
from SEBE.core.apidata_template import ApiDataTemplate

from django.core.mail import send_mail
from django.conf import settings
def login(request):
    ## redirects
    if request.user.is_authenticated:
        return SEBEResponse.create_response(
            request, 
            api_data = ApiDataTemplate('Login Terminated: request already authenticated', ApiDataTemplate.STATUS_INFO).as_dict(),
            is_redirect=True, redirect_to='home-page'
        )
    
    form_template = SEBEFormTemplate(
        'Log In', 'login', '',
        'Forgot Your Password?','','Send Email Verification'
    )

    if request.method == 'POST':
        return auth_ctrl.login(request, form_template)
    
    elif request.method == 'GET':
        ctx = FormContext(LoginForm(), form_template).get_context()
        return SEBEResponse.create_response(
            request, same_resp=True, is_redirect=False, 
            render_from='post-form.html', render_ctx=ctx
        )


def logout(request):

    ## redirects
    if not request.user.is_authenticated:
        return SEBEResponse.create_response(
            request, 
            api_data = ApiDataTemplate('Logout terminated: user is not authenticated', 'info').as_dict(), 
            status_code=406,
            is_redirect=True, redirect_to='accounts-login'
        )

    if request.method == 'GET':
        conform = request.GET.get('conform')
        if conform is None:
            return SEBEResponse.create_response(
                request, api_data = ApiDataTemplate('Logout terminated: use ?conform=true to logout', 'info').as_dict(),
                is_redirect=False, render_from='accounts-logout.html'
            )

        elif conform == 'true':
            auth.logout(request)
            return SEBEResponse.create_response(
                request, api_data = ApiDataTemplate('Logout success').as_dict(),
                message=messages.success(request, f'Logout success'), 
                is_redirect=True, redirect_to='accounts-login'
            )

        else:
            return SEBEResponse.create_response(
                request, api_data = ApiDataTemplate('Logout terminated').as_dict(), 
                is_redirect=True, redirect_to='home-page'
            )

def register(request):
    ## redirects -- only superuser has perm
    is_superuser = False
    if request.user.is_authenticated:
        is_superuser = request.user.is_superuser
            
    if not is_superuser:
        return SEBEResponse.create_response(
            request, api_data = ApiDataTemplate('Error: no permission to register page', 'error').as_dict(), 
            is_redirect=True, redirect_to='admin:login', message=messages.success(request, f'No permission to register page'), 
        )

    form_template = SEBEFormTemplate('Register', 'register')
    
    if request.method == 'POST':
        return auth_ctrl.register(request, form_template)

    elif request.method == 'GET':
        ctx = FormContext(StaffCreationForm(), form_template).get_context()
        return SEBEResponse.create_response(
            request, same_resp=True, is_redirect=False, 
            render_from='post-form.html', render_ctx=ctx
        )
