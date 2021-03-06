from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    return render(request, 'store/home.html')


def about(request):
    return render(request, 'store/about.html')


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/order.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_detail.html', {'product': product})