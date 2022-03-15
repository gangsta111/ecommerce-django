from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.
class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )

    #user           = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order_number   = models.CharField(max_length=20)
    name           = models.CharField(max_length=50)
    phone          = models.CharField(max_length=15)
    subcity        = models.CharField(max_length=50)
    detail_Address = models.CharField(max_length= 100)
    order_note     = models.CharField(max_length=100)
    order_total    = models.FloatField()
    status         = models.CharField(max_length=10, choices=STATUS, default='New')
    ip             = models.CharField(blank=True, max_length=20)
    is_ordered     = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    #user  = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
