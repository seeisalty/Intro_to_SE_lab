from django.urls import path
from . import views

urlpatterns = [
    path('storefront/', views.product_list, name='product_list'),
    path('product_filter/<slug:category_slug>/', views.product_filter, name='product_filter'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('product_search/', views.product_search, name='product_search'),

]