from django.shortcuts import render, reverse, redirect

def login_required(handler):
    login_path_name='accounts-login'
    def wrapper(*args, **kwargs):
        if len(args) < 1 : raise Exception('handler at lease have request argument -- no args found')
        if args[0].user.is_authenticated:
            return handler(*args, **kwargs)
        else :
            return redirect(reverse(login_path_name))
    return wrapper