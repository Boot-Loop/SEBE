from django.urls import path
from drfvg import register_models

## models to register
from .models.inquiry_sheet import InquirySheet
from .models.quotation import Quotation
from .models.progress_tracking import ClientProgress, SupplierProgress

## documents/
urlpatterns = [ ] + register_models(  
    [ InquirySheet, Quotation, ClientProgress, SupplierProgress ],  
    app_name='documents')




