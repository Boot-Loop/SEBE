from django.shortcuts import render, reverse, redirect

from rest_framework.request import Request

## if class based view Request object in args, else args[0] is request
def login_required(handler):
    login_path_name='accounts-login'
    def wrapper(*args, **kwargs):
        if len(args) < 1 : raise Exception('handler at lease have request argument -- no args found')
        request = None
        for arg in args:
            if type(arg) == Request:
                request = arg ; break
        else:
            request = args[0]
        if request.user.is_authenticated:
            return handler(*args, **kwargs)
        else :
            return redirect(reverse(login_path_name))
    return wrapper