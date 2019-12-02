from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from ..models.staff import Staff
from ..models.staff import LoginForm, StaffCreationForm, ForgotPasswordForm

from SEBE.core.context import FormContext

def login(request, form_template):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Success!')
            return redirect('home-page')

        else:
            ctx = FormContext(form, form_template).get_context()
            messages.error(request, f'Authentication failed. (check your username and password)'), 
            return render(request, 'post-form.html', ctx)

    else:
        ctx = FormContext(form, form_template).get_context()
        return render(request, 'post-form.html', ctx)

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

        messages.success(request, f'Staff creation success!'), 
        return redirect( f'/admin/auth/user/{user.id}/change/' )

    else:
        ctx = FormContext(form, form_template).get_context()
        return render(request, 'post-form.html', ctx)

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
            messages.error(request, 'The given email address does not registered'),
            return render(request, 'post-form.html', ctx)
        '''
        token_generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(user.id) ## err
        token = token_generator.make_token(user)
        return HttpResponse(str(token)+'<bt>'+str(uidb64))
        '''

        ## TODO: send mail
        messages.success(request, 'A Password reset email was sent'),
        return redirect('accounts-login')

    else:
        ctx = FormContext(form, form_template).get_context()
        return render(request, 'post-form.html', ctx)
