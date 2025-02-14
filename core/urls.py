from django.urls import path
from .views import dashboard  # Example view

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Example user dashboard
]
