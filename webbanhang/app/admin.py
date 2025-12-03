from django.contrib import admin
from .models import *
from .models import ItemCategory
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)  
admin.site.register(OrderItem)  
admin.site.register(ShippingAddress)
admin.site.register(ItemCategory)
class DataAdmin(admin.ModelAdmin):
    list_display = ('mmr', 'condition', 'odometer')

admin.site.register(Data, DataAdmin)
admin.site.register(Payment_VNPay)

