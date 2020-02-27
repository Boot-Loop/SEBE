from django.contrib import admin

#from .models.staff import Staff
from .models.supplier import Supplier
from .models.client import Client

#admin.site.register(Staff)
admin.site.register(Supplier)
admin.site.register(Client)

