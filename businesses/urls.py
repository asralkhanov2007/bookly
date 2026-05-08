from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<slug:slug>/', views.public_profile, name='public_profile'),
]