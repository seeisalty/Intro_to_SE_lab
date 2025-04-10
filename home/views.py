from django.shortcuts import render
from inventory.models import Category, Product
from django.contrib.auth.decorators import login_required

def homepage(request):
    categories = Category.objects.all() # defines category and product model for dynamic dropdown and feature display
    products = Product.objects.all()
    return render(request, 'home.html', {'categories': categories, 'products': products})  # ✅ Matches the exact template location

def homepage_view(request):
    return render(request, 'home.html')  