from django.shortcuts import render
from .forms import BookingForm
from .models import Booking_detail
from django.shortcuts import redirect, render

# Create your views here.
def booking_success(request):
    booking_info = Booking_detail.objects.last()
    context ={
        'last_detail':booking_info 
    }
    return render(request, 'booking/booking_success.html',context)

# CRUD
def booking_list(request):
    bookings = Booking_detail.objects.all()
    # users_count = users.count()
    context = {
        'booking_list':bookings,
    }
    return render(request,'booking/booking_list.html',context)

def booking_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = BookingForm()
        else:
            booking = Booking_detail.objects.get(pk=id)
            form = BookingForm(instance=booking)
        return render(request, 'booking/booking_form.html', {'form':form})
    else:
        if id==0:
            form = BookingForm(request.POST)
        else:
            booking = Booking_detail.objects.get(pk=id)
            form = BookingForm(request.POST,instance=booking)
        if form.is_valid():
            form.save()
        return redirect('/booking/success')

def booking_delete(request,id):
    booking = Booking_detail.objects.get(pk=id)
    booking.delete()
    return redirect('/booking/list')