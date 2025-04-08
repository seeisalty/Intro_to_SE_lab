from django.db import models
from django.conf import settings
from django.utils.text import slugify

# product categories, so users can filter inventory
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__ (self):
        return self.name

# product model, references a seller (user) and a category (from Categories)
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num_in_stock = models.IntegerField()
    listed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="SellerProducts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="CategoryProducts", null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    image_url = models.TextField(blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Products"
    def __str__ (self):
        return self.name

# table of all products currently in a user's cart
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="CartProducts")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="UserCart")
    num_in_cart = models.IntegerField()
    class Meta:
        verbose_name_plural = "Cart Items"
    def __str__ (self):
        return self.name

