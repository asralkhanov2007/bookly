from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Business, Service, Availability
from .forms import BusinessForm, ServiceForm, AvailabilityForm

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if not hasattr(request.user, 'business'):
        return redirect('businesses:create_business')
    
    business = request.user.business
    bookings = business.bookings.filter(status='pending').order_by('date', 'start_time')
    services = business.services.filter(is_active=True)
    availability = business.availability.all()
    
    return render(request, 'dashboard/dashboard.html', {
        'business': business,
        'bookings': bookings,
        'services': services,
        'availability': availability,
    })

@login_required
def create_business(request):
    if hasattr(request.user, 'business'):
        return redirect('businesses:dashboard')

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = request.user
            business.save()
            messages.success(request, 'Business created! Now add your services.')
            return redirect('businesses:dashboard')
    else:
        form = BusinessForm()

    return render(request, 'dashboard/create_business.html', {'form': form})

@login_required
def add_service(request):
    business = get_object_or_404(Business, owner=request.user)

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.business = business
            service.save()
            messages.success(request, 'Service added successfully!')
            return redirect('businesses:dashboard')
    else:
        form = ServiceForm()

    return render(request, 'dashboard/add_service.html', {'form': form})

@login_required
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id, business__owner=request.user)
    service.delete()
    messages.success(request, 'Service deleted.')
    return redirect('businesses:dashboard')

@login_required
def set_availability(request):
    business = get_object_or_404(Business, owner=request.user)

    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.business = business
            availability.save()
            messages.success(request, 'Availability updated!')
            return redirect('businesses:dashboard')
    else:
        form = AvailabilityForm()

    return render(request, 'dashboard/set_availability.html', {
        'form': form,
        'availability': business.availability.all()
    })

def public_profile(request, slug):
    business = get_object_or_404(Business, slug=slug)
    services = business.services.filter(is_active=True)
    availability = business.availability.filter(is_available=True)
    return render(request, 'public/profile.html', {
        'business': business,
        'services': services,
        'availability': availability,
    })