from django.db import models

class Order(models.Model):
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed
