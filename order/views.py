import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .models import Order, OrderItem
from inventory.models import Cart
from decimal import Decimal, ROUND_HALF_UP

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY # secret key

# Function to create sheckout session
def create_checkout_session(request):
    cart_items = Cart.objects.filter(buyer=request.user)
    line_items = []
    total_price = 0

    # Get item data in cart
    for item in cart_items:
        item_price = item.product.price * item.num_in_cart
        total_price += item_price
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),  # convert to cents
            },
            'quantity': item.num_in_cart,
        })

# Create session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
        customer_email=request.user.email,
    )

    return redirect(session.url)

# Handles actions after successful payment, clearing cart, creating order, etc.
def payment_success(request):
    # Retrieving session id if applicable
    stripe_session_id = request.GET.get('session_id')

    if not stripe_session_id:
        return HttpResponse("Missing session_id", status=400)

    try:
        session = stripe.checkout.Session.retrieve(stripe_session_id)
    except stripe.error.InvalidRequestError as e:
        return HttpResponse(f"Invalid session_id: {str(e)}", status=400)
    
    # Prevent crashes upon page reload after making order
    existing_order = Order.objects.filter(stripe_payment_intent_id=session.payment_intent).first()

    if existing_order:
        order = existing_order
    else:
        # Create the order
        order = Order.objects.create(
            buyer=request.user,
            total_price=session.amount_total / 100,
            stripe_payment_intent_id=session.payment_intent
        )

        # Add items to the order
        cart_items = Cart.objects.filter(buyer=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.num_in_cart,
                price=item.product.price
            )

        # Clear cart
        cart_items.delete()

    # Compute total price with tax
    tax_rate = Decimal('1.07')
    total_price_decimal = Decimal(str(order.total_price))
    total_with_tax = (total_price_decimal * tax_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
  
    return render(request, 'payment_success.html', {'order_id': order.id, 'total_amount': total_with_tax})

#payment canceled view to render canceled payment page
def payment_cancel(request):
    return render(request, 'payment_cancel.html')