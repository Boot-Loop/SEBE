from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse

from ..controls import auth_ctrl
from ..models.staff import LoginForm, StaffCreationForm, ForgotPasswordForm

from SEBE.core.form_template import SEBEFormTemplate
from SEBE.core.context import FormContext
##from SEBE.core.sebe_response import SEBEResponse
from SEBE.core.apidata_template import ApiDataTemplate


def login(request):

    ## redirects
    if request.user.is_authenticated:
        return redirect('home-page')
    
    form_template = SEBEFormTemplate(
        'Log In', 'login', has_footer=True, footer_link_text='Forgot Your Password?', footer_link_href=reverse('accounts-forgot_password'),
    )

    ## post
    if request.method == 'POST':
        return auth_ctrl.login(request, form_template)
    
    ## get
    elif request.method == 'GET':
        ctx = FormContext(LoginForm(), form_template).get_context()
        return render(request, 'post-form.html', ctx)


def logout(request):

    ## redirects
    if not request.user.is_authenticated:
        return redirect('accounts-login')

    ## get -- no post
    if request.method == 'GET':
        conform = request.GET.get('conform')
        if conform is None:
            return render(request, 'accounts-logout.html' )

        elif conform == 'true':
            auth.logout(request)
            messages.success(request, f'Logout success')
            return redirect('accounts-login')

        else:
            return redirect('home-page')

def register(request):
    ## redirects -- only superuser has perm
    is_superuser = False
    if request.user.is_authenticated:
        is_superuser = request.user.is_superuser
            
    if not is_superuser:
        messages.success(request, f'No permission to register page')
        return redirect('admin:login')

    form_template = SEBEFormTemplate('Register', 'register')
    
    ## post
    if request.method == 'POST':
        return auth_ctrl.register(request, form_template)

    ## get
    elif request.method == 'GET':
        ctx = FormContext(StaffCreationForm(), form_template).get_context()
        return render(request, 'post-form.html', ctx)

def forgot_password(request):
    ## redirects
    if request.user.is_authenticated:
        return redirect('home-page')

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
        return render(request, 'post-form.html', ctx)