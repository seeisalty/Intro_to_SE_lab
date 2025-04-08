from django.shortcuts import render, get_object_or_404
from inventory.models import Product, Category
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

def product_filter(request, category_slug):
    reverse_categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product_filter.html', {'category': category, 'products': products, 'reverse_categories': reverse_categories})

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    categories = Category.objects.all()
    return render(request, 'product_detail.html', {'product': product, 'categories': categories})

def product_search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    return render(request, 'product_search.html', {'products': products, 'query': query})

