from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    """
    Shows home page.
    """
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "home.html", {"products": products})


def about(request):
    """
    Shows about page.
    """
    return render(request, "store/about.html")


def category_list(request, category_slug=None):
    """
    Shows category list for category slug and its descendants.
    """
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(
        request,
        "store/category.html",
        {"category": category, "products": products},
    )


def product_all(request):
    """
    Displays all products.
    """
    products = Product.objects.all()
    return render(request, "store/all_products.html", {"products": products})


def product_detail(request, slug):
    """
    Displays a single product detail page.
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/product_detail.html", {"product": product})
