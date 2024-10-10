from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username
    
class Machinery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    


# users/models.py
from django.db import models
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    machinery = models.ForeignKey(
        'booking.Machinery', 
        on_delete=models.CASCADE
    )
    booking_date = models.DateField()  # Date field for the booking date
    return_date = models.DateField()   # Date field for when the machinery is expected to be returned
    status = models.CharField(
        max_length=20, 
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')],
        default='pending'
    )
    notes = models.TextField(
        blank=True, 
        null=True, 
        help_text="Optional notes regarding the booking"
    )

    def __str__(self):
        return f"{self.user} booked {self.machinery} on {self.booking_date}"
