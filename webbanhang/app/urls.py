from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.home, name= "home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('detail/', views.detail, name="detail"),
    path('predictions/', views.predictions, name='predictions'),
    path('index/', views.index, name="index"),
    path('pay', views.indexs, name='indexs'),
    path('payment', views.payment, name='payment'),
    path('payment_ipn',views.payment_ipn, name='payment_ipn'),
    path('payment_return',views.payment_return, name='payment_return'),
    path('query',views.query, name='query'),
    path('refund',views.refund, name='refund'),
    
]