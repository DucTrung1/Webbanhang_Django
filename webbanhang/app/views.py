from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.views.generic import FormView 
from django.views.generic import TemplateView
from .forms import DataForm

def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictions')
    else:
        form = DataForm()
    context = {'form': form}  # Chỉnh sửa tên biến thành 'form'
    return render(request, 'app/index.html', context)




def predictions(request):
    predicted_sales = Data.objects.all()
    context = {
        'predicted_sales': predicted_sales
    }
    
    return render(request, 'app/predictions.html',context)

#@api_view(["POST"])

def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    id = request.GET.get('id', '')
    products = Product.objects.filter(id=id)    
    categories = Category.objects.filter(is_sub=False)

    context = {'products':products,'categories':categories,'items': items, 'order': order,'cartItems': cartItems}
    return render(request, 'app/detail.html', context)

def category(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    context = {'products': products, 'cartItems': cartItems,'categories': categories, 'products': products, 'active_category_slug': active_category}
    return render(request, 'app/category.html', context)

 
 
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    return render(request, 'app/search.html', {"searched": searched, "keys": keys,'products': products, 'cartItems': cartItems})

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    context = {'form':form}
    return render(request, 'app/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: messages.info(request, 'user or password not correct!')

    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login') 
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=False)
    
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems,'categories':categories}
    return render(request, 'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub=False)

    context = {'categories':categories,'items': items, 'order': order,'cartItems': cartItems}
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = OrderItem.objects.filter(order=order)
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order,'cartItems': cartItems}
    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action =='remove':
        orderItem.quantity -= 1 
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('added', safe = False)


