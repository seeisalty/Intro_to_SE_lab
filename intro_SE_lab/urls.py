from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from home import views as home_views

urlpatterns = [
    path('', home_views.homepage_view, name='homepage'),  # Points to the homepage view in the home app
    path('sign-up/', include('userauth.urls')),  # Make sure this includes the userauth urls
    path('login/', include('userauth.urls')),  # Login URL
    path('logout/', include('userauth.urls')),  # Logout URL
    path('home/', include('home.urls')),  # Home page (after login)
    path('storefront/', include('storefront.urls')),  # Storefront URL
    path('admin/', admin.site.urls),  # Admin panel
]
