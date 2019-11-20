from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .core.apidata_template import ApiDataTemplate
##from .core.sebe_response import SEBEResponse

@login_required
def home(request):
    return render(request, 'home.html')