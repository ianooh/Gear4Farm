# booking/admin.py
from django.contrib import admin
from users.models import Booking  # Correct import
from .models import Machinery

@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'availability')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'machinery', 'booking_date', 'status')

