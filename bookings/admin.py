from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'business', 'service', 'date', 'start_time', 'status']
    list_filter = ['status', 'business', 'date']
    search_fields = ['customer_name', 'customer_email']
    list_editable = ['status']