from django.shortcuts import get_object_or_404, render

from .models import *


def home(request):
    return render(request, "store/home.html")


def about(request):
    return render(request, "store/about.html")


def product_all(request):
    products = Product.objects.all()
    return render(request, "store/order.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/product_detail.html", {"product": product})
