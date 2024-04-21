from django.contrib.auth.models import User
from django.db import models
from opply_project.utils import TimeStampedModel


class Customer(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
