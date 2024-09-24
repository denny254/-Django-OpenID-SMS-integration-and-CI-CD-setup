from django.contrib import admin
from .models import Order, Customer

# Register your models here.

admin.site.register(Order)
admin.site.register(Customer)