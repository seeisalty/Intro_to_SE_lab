from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('home.urls')),  # Home page  # Points to the homepage view in the home app
    path('sign-up/', include('userauth.urls')),  # Make sure this includes the userauth urls
    path('login/', include('userauth.urls')),  # Login URL
    path('logout/', include('userauth.urls')),  # Logout URL
    path('storefront/', include('storefront.urls')),  # Storefront URL
    path('admin/', admin.site.urls),  # Admin panel
]
