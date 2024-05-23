from django import forms
from .models import Data
from django import forms
from .models import ShippingAddress

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','date_block_num', 'shop_id', 'item_id', 'item_price', 'item_cnt_day']


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress  # Chỉ định mô hình là ShippingAddress
        fields = ['user', 'email', 'address', 'city', 'state', 'mobile']

        
