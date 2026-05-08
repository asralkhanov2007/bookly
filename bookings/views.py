from django.shortcuts import render

# Create your views here.

def book_service(request, business_slug, service_id):

    return render(request, 'public/book.html')

def booking_confirmation(request, booking_id):

    return render(request, 'public/confirmation.html')