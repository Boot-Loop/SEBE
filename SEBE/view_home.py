from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .core.apidata_template import ApiDataTemplate

@login_required
def home(request):
    return render(request, 'home.html')