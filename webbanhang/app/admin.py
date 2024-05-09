from django.contrib import admin
from .models import *
from .models import ItemCategory
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)  # Sửa chính tả từ Oder thành Order
admin.site.register(OrderItem)  # Sửa chính tả từ OderItem thành OrderItem
admin.site.register(ShippingAddress)
admin.site.register(ItemCategory)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name','date_block_num','shop_id','item_id','item_price','item_cnt_day','predictions')
admin.site.register(Data, DataAdmin)
