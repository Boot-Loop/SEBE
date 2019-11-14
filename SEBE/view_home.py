from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .core.apidata_template import ApiDataTemplate
from .core.sebe_response import SEBEResponse

@login_required
def home(request):
    return SEBEResponse.create_response(
            request, 
            api_data = ApiDataTemplate('Welcome to SEBE home page!', ApiDataTemplate.STATUS_INFO).as_dict(), 
            status_code=200,
            is_redirect=False, render_from='home.html'
        )