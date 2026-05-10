from django.contrib import admin
from .models import Business, Service, Availability

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'business', 'duration', 'price', 'is_active']
    list_filter = ['is_active', 'business']

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['business', 'day_of_week', 'start_time', 'end_time', 'is_available']