from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name','date_block_num', 'shop_id', 'item_id', 'item_price', 'item_cnt_day']
