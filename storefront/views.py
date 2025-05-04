from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import Product, Category, Cart
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

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

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(buyer=request.user)
    
    # Add subtotal attribute to each item
    for item in cart_items:
        item.subtotal = item.product.price * item.num_in_cart

    subtotal_price = sum(item.subtotal for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'subtotal_price': subtotal_price, })

# Update cart upon addition or subtraction of the quantity of an item
@require_POST
@login_required
def update_cart(request):
    cart_item_id = request.POST.get('cart_item_id')
    action = request.POST.get('action')  # 'increment' or 'decrement'

    try:
        cart_item = Cart.objects.get(id=cart_item_id, buyer=request.user)
        if action == 'increment':
            if cart_item.num_in_cart < cart_item.product.num_in_stock:
                cart_item.num_in_cart += 1
                cart_item.save()
            else:
                return JsonResponse({
                    'success': False,
                    'error': "Cannot increase quantity. Not enough stock."
                })
            
        elif action == 'decrement':
            if cart_item.num_in_cart > 1:
                cart_item.num_in_cart -= 1
                cart_item.save()

        subtotal = cart_item.product.price * cart_item.num_in_cart
        total_price = sum(item.product.price * item.num_in_cart for item in Cart.objects.filter(buyer=request.user))

        return JsonResponse({
            'success': True,
            'new_quantity': cart_item.num_in_cart,
            'item_subtotal': f"{subtotal:.2f}",
            'total_price': f"{total_price:.2f}",
        })
    except Cart.DoesNotExist:
        return JsonResponse({'success': False}, status=404)

# Add item to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Only buyers can add to cart
    if request.user.role != 'buyer':
        return redirect('product_list')

    cart_item, created = Cart.objects.get_or_create(
        buyer=request.user,
        product=product,
        defaults={'num_in_cart': 1}
    )
    if not created:
        cart_item.num_in_cart += 1
        cart_item.save()

    return redirect('view_cart')

# Remove item from cart
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, buyer=request.user)
    cart_item.delete()
    return redirect('view_cart')

def get_cart_count(user):
    if user.is_authenticated:
        return Cart.objects.filter(buyer=user).count()
    return 0
