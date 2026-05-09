from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/create/', views.create_business, name='create_business'),
    path('dashboard/services/add/', views.add_service, name='add_service'),
    path('dashboard/services/delete/<int:service_id>/', views.delete_service, name='delete_service'),
    path('dashboard/availability/', views.set_availability, name='set_availability'),
    path('<slug:slug>/', views.public_profile, name='public_profile'),
]