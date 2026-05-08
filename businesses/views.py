from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'home.html')

def dashboard(request):

    return render(request, 'dashboard/dashboard.html')

def public_profile(request, slug):
    
    return render(request, 'public/profile.html')