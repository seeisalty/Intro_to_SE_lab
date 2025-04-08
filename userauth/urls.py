from django.urls import path 
from userauth import views
from .views import settings_view

urlpatterns = [
    path('sign-up/', views.register_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('settings/', settings_view, name='settings'),  # ✅ add this
    path('logout/', views.logout_view, name='logout'),

]