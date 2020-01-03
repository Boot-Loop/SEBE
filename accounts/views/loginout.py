from django.shortcuts import render, redirect
from django.contrib.auth.models import auth ## for login and logout
from django.contrib.auth import authenticate ## get user

## from django.contrib import messages

from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )

def login(request):

    ## redirects
    if request.user.is_authenticated:
        return redirect('home-page')

    ## get
    elif request.method == 'GET':
        return render(request, 'login.html')

    ## post
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                ## messages.success(request, 'Login Success!')
                return redirect('home-page')
            else:
                return render(request, 'login.html', {'username':username, 'error_message':"Invalid Username or Password" })
        else:
            return render(request, 'login.html', {"error_message":"Invalid Login Form"} )
    
    


def logout(request):
    auth.logout(request)
    ## messages.success(request, f'Logout success')
    return redirect('accounts-login')
