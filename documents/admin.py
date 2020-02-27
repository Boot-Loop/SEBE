from django.contrib import admin

from .models.inquiry_sheet import InquirySheet
from .models.quotation import Quotation
from .models.progress_tracking import ClientProgress, SupplierProgress

admin.site.register(InquirySheet)
admin.site.register(Quotation)
admin.site.register(ClientProgress)
admin.site.register(SupplierProgress)
