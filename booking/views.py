from rest_framework import viewsets
from .models import Machinery, Booking
from .serializers import MachinerySerializer, BookingSerializer

class MachineryViewSet(viewsets.ModelViewSet):
    queryset = Machinery.objects.all()
    serializer_class = MachinerySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
