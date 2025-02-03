from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Warehouse', 'Warehouse Personnel'),
        ('VehicleManagement', 'Vehicle Management Team'),
        ('Operations', 'Operations Team'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Warehouse')

    def __str__(self):
        return self.username
