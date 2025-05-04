from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product_filter/<slug:category_slug>/', views.product_filter, name='product_filter'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('product_search/', views.product_search, name='product_search'),
<<<<<<< HEAD
     path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
=======
    path('seller_panel/', views.seller_panel, name='seller_panel'),
    path('product_edit/<slug:product_slug>/', views.product_edit, name='product_edit'),
    path('product_add/', views.product_add, name='product_add'),
    
>>>>>>> 484de5de (seller panel added)

]