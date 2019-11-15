
## response handler for api and user
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

class SEBEResponse:

    ''' message is messages instance : messages.success('success message') won't be used just to call '''
    @staticmethod
    def create_response( request, 
            api_data=dict(), status_code=200,
            message = None, is_redirect = True, redirect_to = 'home-page', render_from='', render_ctx = dict(),
            same_resp = False ## user and api get same response
        ): 

        ## set api_resp
        api_resp = False 
        if request.method == 'GET':
            if request.GET.get('api') is not None:
                api_resp = True
        elif request.method == 'POST':
            if request.POST.get('api') is not None:
                api_resp = True

        
        
        ## api response
        if api_resp and not same_resp:
            resp = JsonResponse(api_data)
            resp.status_code = status_code
            return resp
            
        ## user response
        else:
            if is_redirect:
                return redirect(redirect_to)
            else:
                return render(request, render_from, render_ctx)
                

    
    
