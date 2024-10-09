from django.db import models
from django.contrib.auth.models import User

class Machinery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machinery = models.ForeignKey(Machinery, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.machinery}'
