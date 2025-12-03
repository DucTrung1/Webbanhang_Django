import collections
from tkinter import CENTER
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
import torch
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

import torch
import torch.nn as nn
class Payment_VNPay(models.Model):
    order_id = models.CharField(max_length=50, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    order_desc = models.CharField(max_length=200,null=True, blank=True)
    vnp_TransactionNo = models.CharField(max_length=200,null=True, blank=True)
    vnp_ResponseCode = models.CharField(max_length=200,null=True, blank=True)
   


class PaymentForm(forms.Form):
    order_id = forms.CharField(max_length=50)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)


class Data(models.Model):
    mmr = models.FloatField()
    condition = models.FloatField()
    odometer = models.FloatField()

    def __str__(self):
        return f"MMR: {self.mmr}, Condition: {self.condition}, Odometer: {self.odometer}"

#category(danh muc)
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'sub_categories', null = True, blank = True)
    is_sub = models.BooleanField(default = False)
    name = models.CharField(max_length = 200, null = True)
    slug = models.SlugField(max_length = 200, unique = True)
    def __str__(self):
        return self.name
    
class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    category_id = models.IntegerField()

    def __str__(self):
        return self.name

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']



class Product(models.Model):
    category = models.ManyToManyField(Category, related_name = 'product')
    name = models.CharField(max_length=200, null=True)
    gia = models.IntegerField()
    digital = models.BooleanField(default=False)
    image = models.ImageField()
    detail = models.TextField(null=True,blank=True)
    feature_vector = models.TextField(null=True, blank=True)  


    def __str__(self):
        return self.name 

    @property   
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        if self.product is not None:  
            total = self.product.gia * self.quantity
            return total
        else:
            return 0


def validate_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError("Email must end with '@gmail.com'.")

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.CharField(max_length=100, validators=[validate_email])
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=13, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
