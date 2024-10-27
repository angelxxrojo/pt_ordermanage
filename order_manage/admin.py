# Register your models here.
from django.contrib import admin
from .models import Inventory, Order

# Registrar el modelo Inventory
admin.site.register(Inventory)

# Registrar el modelo Order
admin.site.register(Order)
