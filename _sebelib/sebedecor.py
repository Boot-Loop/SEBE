from django.shortcuts import render, reverse, redirect

from rest_framework.request import Request
from django.core.handlers.wsgi import WSGIRequest

LOGIN_PATH_NAME='accounts-login'

## if class based view Request object in args, else args[0] is request
def login_required(handler):
    def wrapper(*args, **kwargs):
        if len(args) < 1 : raise Exception('handler at lease have request argument -- no args found')
        request = None
        for arg in args:
            if type(arg) == Request or type(arg) == WSGIRequest:
                request = arg ; break
        else:
            raise Exception('no django rest framework request found')
        if request.user.is_authenticated:
            return handler(*args, **kwargs)
        else :
            return redirect(reverse(LOGIN_PATH_NAME))
    return wrapper