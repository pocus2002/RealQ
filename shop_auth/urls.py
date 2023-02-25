from django.contrib import admin
from django.urls import path
from .views import CreateShopUser, ShopLoginView, shop_logout

app_name = 'shop_auth'

urlpatterns = [
    path('create/', CreateShopUser.as_view(), name='create_user'),
    path('login/', ShopLoginView.as_view(), name='login'),
    path('logout/', shop_logout, name='logout'),
]