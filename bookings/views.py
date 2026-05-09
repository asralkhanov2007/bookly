from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from businesses.models import Business, Service
from .models import Booking
from .forms import BookingForm

def book_service(request, business_slug, service_id):
    business = get_object_or_404(Business, slug=business_slug)
    service = get_object_or_404(Service, id=service_id, business=business, is_active=True)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.business = business
            booking.service = service

            # Calculate end time based on service duration
            date = form.cleaned_data['date']
            start_time = request.POST.get('start_time')

            if not start_time:
                form.add_error(None, 'Please select a time slot.')
                return render(request, 'public/book.html', {
                    'form': form, 'business': business, 'service': service
                })

            start_dt = datetime.strptime(start_time, '%H:%M')
            end_dt = start_dt + timedelta(minutes=service.duration)

            booking.start_time = start_dt.time()
            booking.end_time = end_dt.time()

            # Check for double booking
            existing = Booking.objects.filter(
                business=business,
                date=date,
                start_time=booking.start_time,
                status__in=['pending', 'confirmed']
            ).exists()

            if existing:
                form.add_error(None, 'This time slot is already booked. Please choose another.')
                return render(request, 'public/book.html', {
                    'form': form, 'business': business, 'service': service
                })

            booking.save()
            return redirect('bookings:confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'public/book.html', {
        'form': form,
        'business': business,
        'service': service,
    })

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    return render(request, 'public/confirmation.html', {'booking': booking})