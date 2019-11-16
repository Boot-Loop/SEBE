from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate

from ..models.staff import LoginForm, StaffCreationForm, Staff

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
            return SEBEResponse.create_response(
                request, 
                api_data = ApiDataTemplate('Authentication Error: user not exists', ApiDataTemplate.STATUS_ERROR).as_dict(), 
                status_code=404,
                message=messages.error(request, f'Authentication failed. (check your username and password)'), 
                is_redirect=True, redirect_to='accounts-login'
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
