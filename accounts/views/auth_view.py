from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import auth

from ..controls import auth_ctrl

from ..models.staff import LoginForm
from SEBE.core.form_template import SEBEFormTemplate
from SEBE.core.context import FormContext

from SEBE.core.sebe_response import SEBEResponse
from SEBE.core.apidata_template import ApiDataTemplate


def login(request):

    ## redirects
    if request.user.is_authenticated:
        return SEBEResponse.create_response(
                    request, 
                    api_data = ApiDataTemplate('Login Terminated: request already authenticated', ApiDataTemplate.STATUS_INFO).as_dict(), 
                    status_code=200,
                    is_redirect=True, redirect_to='home-page'
                )

    form_template = SEBEFormTemplate(
            'Log In', 'login', '',
            'Forgot Your Password?','','Send Email Verification'
    )

    if request.method == 'POST':
        return auth_ctrl.login(request)
    
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
                    api_data = ApiDataTemplate('Logout terminated: user is not authenticated', ApiDataTemplate.STATUS_INFO).as_dict(), 
                    status_code=406,
                    is_redirect=True, redirect_to='accounts-login'
                )

    if request.method == 'GET':
        conform = request.GET.get('conform')
        if conform is None:
            return SEBEResponse.create_response(
                    request, 
                    api_data = ApiDataTemplate('Logout terminated: use ?conform=true to logout', ApiDataTemplate.STATUS_INFO).as_dict(), 
                    status_code=200,
                    is_redirect=False, render_from='accounts-logout.html'
                )

        elif conform == 'true':
            auth.logout(request)
            return SEBEResponse.create_response(
                    request, 
                    api_data = ApiDataTemplate('Logout success', ApiDataTemplate.STATUS_SUCCESS).as_dict(), 
                    status_code=200,
                    message=messages.success(request, f'Logout success'), 
                    is_redirect=True, redirect_to='accounts-login'
                )
        else:
            return SEBEResponse.create_response(
                    request, 
                    api_data = ApiDataTemplate('Logout terminated', ApiDataTemplate.STATUS_SUCCESS).as_dict(), 
                    status_code=200,
                    is_redirect=True, redirect_to='home-page'
                )
