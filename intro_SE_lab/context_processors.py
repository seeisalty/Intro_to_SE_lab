from inventory.models import Cart

# Function to make cart count globally available
def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(buyer=request.user).count()
    else:
        count = 0
    return {'cart_count': count}