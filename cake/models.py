from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin



class Signup(AbstractUser,PermissionsMixin):
    full_name=models.CharField(max_length=50)
    username=models.EmailField(unique=True)
    phone_number = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=10)
    location=models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.full_name
    

class ContactFormEntry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    how_did_you_find_us = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name=models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category"  # Singular name
        verbose_name_plural = "Categories"  # Plural name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Price based on weight (modify as needed)
    price_half_kg = models.IntegerField()
    price_one_kg = models.IntegerField()
    price_one_and_half_kg = models.IntegerField()

    # Eggless option
    
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    # Add more fields as needed

    def __str__(self):
        return self.name

