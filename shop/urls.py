from django.contrib import admin
from django.urls import path
from .views import index, ShopItemListView

app_name = 'shop'

urlpatterns = [
    path('item', ShopItemListView.as_view(), name='shop_main'),
]