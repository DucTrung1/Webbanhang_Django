from django import forms
from .models import Data
from django import forms
from .models import ShippingAddress

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['mmr', 'condition', 'odometer']
        widgets = {
            'mmr': forms.NumberInput(attrs={'class': 'form-control'}),
            'condition': forms.NumberInput(attrs={'class': 'form-control'}),
            'odometer': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress  # Chỉ định mô hình là ShippingAddress
        fields = ['user', 'email', 'address', 'city', 'state', 'mobile']

        
