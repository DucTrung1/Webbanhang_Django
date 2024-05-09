from tkinter import CENTER
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
import joblib


class Data(models.Model):
    date_block_num = models.IntegerField()
    shop_id = models.IntegerField()
    item_id = models.IntegerField()
    item_price = models.FloatField()
    item_cnt_day = models.FloatField()
    name = models.CharField(max_length=255)
    predictions = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('app/templates/app/ml_model.joblib')
        self.predictions = ml_model.predict(
            [[self.date_block_num, self.shop_id, self.item_id,self.item_price,self.item_cnt_day]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date_block_num']

    def __str__(self):
        return self.name

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
    gia = models.FloatField()
    digital = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    detail = models.TextField(null=True,blank=True)

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
        total = self.product.gia * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=13, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
