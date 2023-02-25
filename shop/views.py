from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

# Create your views here.

def index(request):
    context = {}
    return render(request, 'shop/index.html', context)


class ShopItemListView(ListView):
    model = Item
    template_name = 'shop/shop_main.html'
    paginate_by = 3