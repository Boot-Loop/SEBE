from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse

from ..controls import auth_ctrl
from ..models.staff import LoginForm, StaffCreationForm, ForgotPasswordForm

from SEBE.core.form_template import SEBEFormTemplate
from SEBE.core.context import FormContext
from SEBE.core.sebe_response import SEBEResponse
from SEBE.core.apidata_template import ApiDataTemplate


def login(request):

    ## redirects
    if request.user.is_authenticated:
        return SEBEResponse.create_response(
            request, is_redirect=True, redirect_to='home-page',
            api_data = ApiDataTemplate('Login Terminated: request already authenticated', ApiDataTemplate.STATUS_INFO).as_dict()
        )
    
    form_template = SEBEFormTemplate(
        'Log In', 'login', has_footer=True, footer_link_text='Forgot Your Password?', footer_link_href=reverse('accounts-forgot_password'),
    )

    ## post
    if request.method == 'POST':
        return auth_ctrl.login(request, form_template)
    
    ## get
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
            request,  is_redirect=True, redirect_to='accounts-login', status_code=406,
            api_data = ApiDataTemplate('Logout terminated: user is not authenticated', 'info').as_dict(), 
        )

    ## get -- no post
    if request.method == 'GET':
        conform = request.GET.get('conform')
        if conform is None:
            return SEBEResponse.create_response(
                request, is_redirect=False, render_from='accounts-logout.html',
                api_data = ApiDataTemplate('Logout terminated: use ?conform=true to logout', 'info').as_dict(),
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
    
    ## post
    if request.method == 'POST':
        return auth_ctrl.register(request, form_template)

    ## get
    elif request.method == 'GET':
        ctx = FormContext(StaffCreationForm(), form_template).get_context()
        return SEBEResponse.create_response(
            request, same_resp=True, is_redirect=False, 
            render_from='post-form.html', render_ctx=ctx
        )

def forgot_password(request):
    ## redirects
    if request.user.is_authenticated:
        return SEBEResponse.create_response(
            request, is_redirect=True, redirect_to='home-page',
            api_data = ApiDataTemplate('forgot-password page not available: user is authenticated', 'info').as_dict()
        )

    form_template = SEBEFormTemplate('Fogot Password', 'send email', 
        safe_html_message = "<p>Don't worry we'll send you a password reset link to your email." + 
            f"<br><small class='text-muted'>*the link only valid for { '{ TODO }' } hours</small></p>"
    )

    ## post
    if request.method == 'POST':
        return auth_ctrl.forgot_password(request, form_template)

    ## get
    elif request.method == 'GET':
        ctx = FormContext(ForgotPasswordForm(), form_template).get_context()
        return SEBEResponse.create_response(
            request, same_resp=True, is_redirect=False, 
            render_from='post-form.html', render_ctx=ctx
        )