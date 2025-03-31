from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom user that extends abstract user model 
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
    email = models.EmailField(unique=True) # only one account per email

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = ['username']  # keep username as required field

    def __str__(self):
        return f"{self.email} ({self.role})"