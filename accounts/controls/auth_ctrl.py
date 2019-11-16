from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate

from ..models.staff import Staff
from ..models.staff import LoginForm, StaffCreationForm, ForgotPasswordForm

from SEBE.core.apidata_template import ApiDataTemplate
from SEBE.core.sebe_response import SEBEResponse
from SEBE.core.context import FormContext

def login(request, form_template):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return SEBEResponse.create_response(
                request, api_data=ApiDataTemplate('Login success'),
                is_redirect=True, redirect_to='home-page'
            )

        else:
            ctx = FormContext(form, form_template).get_context()
            return SEBEResponse.create_response(
                request, status_code=400,
                api_data = ApiDataTemplate('Authentication Error: user not exists', ApiDataTemplate.STATUS_ERROR).as_dict(), 
                message=messages.error(request, f'Authentication failed. (check your username and password)'), 
                is_redirect=False, render_from='post-form.html', render_ctx=ctx
            )

    else:
        ctx = FormContext(form, form_template).get_context()
        return SEBEResponse.create_response(
            request, api_data=ApiDataTemplate({'invalid form errors': form.errors}), status_code=400,
            is_redirect=False, render_from='post-form.html', render_ctx=ctx
        )

def register(request, form_template):
    form = StaffCreationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email    = form.cleaned_data.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_staff = True
        staff = Staff.objects.create(user=user, email=email)
        #auth.login(request, user)

        return SEBEResponse.create_response(
            request, api_data=ApiDataTemplate('Staff creation success'),
            is_redirect=True, redirect_to=f'/admin/auth/user/{user.id}/change/', ## edit page TODO: change this (add permissinos auto)
            message=messages.success(request, f'Staff creation success!'), 
        )

    else:
        ctx = FormContext(form, form_template).get_context()
        return SEBEResponse.create_response(
            request, api_data=ApiDataTemplate({'invalid form errors': form.errors}), status_code=400,
            is_redirect=False, render_from='post-form.html', render_ctx=ctx
        )

## temp
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

def forgot_password(request, form_template):

    form = ForgotPasswordForm(request.POST)
    if form.is_valid():

        ## check user exists
        email = form.cleaned_data.get('email')
        try:
            user = Staff.objects.get(email=email).user
        except Staff.DoesNotExist:
            ctx = FormContext(form, form_template).get_context()
            return SEBEResponse.create_response(
                request, api_data=ApiDataTemplate(message="Error: the given email address does not registered", status='error'),
                message=messages.error(request, 'The given email address does not registered'),
                is_redirect=False, render_from='post-form.html', render_ctx=ctx
            )
        '''
        token_generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(user.id) ## err
        token = token_generator.make_token(user)
        return HttpResponse(str(token)+'<bt>'+str(uidb64))
        '''

        ## TODO: send mail

        return SEBEResponse.create_response(
            request, api_data=ApiDataTemplate(message="A Password reset email was sent"),
            message=messages.success(request, 'A Password reset email was sent'),
            is_redirect=True, redirect_to='accounts-login'
        )

    else:
        ctx = FormContext(form, form_template).get_context()
        return SEBEResponse.create_response(
            request, api_data=ApiDataTemplate({'invalid form errors': form.errors}), status_code=400,
            is_redirect=False, render_from='post-form.html', render_ctx=ctx
        )
