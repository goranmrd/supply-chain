from django.db import models
from product.models import Product
from customer.models import Customer
from opply_project.utils import TimeStampedModel
from decimal import Decimal


class Order(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return Decimal(self.price) * Decimal(self.quantity)
