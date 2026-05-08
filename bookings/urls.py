from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('<slug:business_slug>/book/<int:service_id>/', views.book_service, name='book_service'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='confirmation'),
]