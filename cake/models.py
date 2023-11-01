from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator



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
    category_dp = models.ImageField(blank=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price_per_piece = models.PositiveIntegerField(blank=True,default=1)
    price_half_kg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)],blank=True,null=True, default=None)
    price_one_kg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)],blank=True,null=True, default=None)
    price_one_and_half_kg = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)],blank=True,null=True, default=None)
    eggless = models.BooleanField(default=False)    
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    image1 = models.ImageField(upload_to="item_image",null=True,blank=True)
    image2 = models.ImageField(upload_to="item_image",null=True,blank=True)
    image3 = models.ImageField(upload_to="item_image",null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = "Products"

