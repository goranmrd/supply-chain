from django.db import models
from opply_project.utils import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
