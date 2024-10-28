from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
@login_required
def make_reservation(request):
    # empty list to store available times if reservation time is already booked
    available_times = []
    # If submitting a form
    if request.method == 'POST': 
        form = ReservationForm(request.POST)
        if form.is_valid():
            # get the cleaned new reservation date and time 
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            # combine the date and time into datetime
            reservation_datetime = timezone.make_aware(
                datetime.combine(
                reservation_date,
                datetime.strptime(reservation_time, "%H:%M").time()
                ))
            # the reservation ends after two hours
            end_time = reservation_datetime + timedelta(hours=1, minutes=45)

            # checks for overlapping reservations for the new reseervation
            # generates a list of all of the times the restaraunt is open
            # gets all reservations for the chosen date
            # add all times to available times that arent linked to an existing reservation
            if check_overlapping_reservations():
                all_times = generate_all_times()
                available_times = filter_available_times()

            # Error message to tell user that the time is unavailable
            form.add_error(None, "This reservation is unavaiable")

        # if form is valid else
        else:
            # new reservation is okay and is saved
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('home')

    # if request method else
    else:
        form = ReservationForm() # If loading the page, load the form
    return render(request, 'reservations/make_reservation.html', {'form': form, 'available_times': available_times})

def check_overlapping_reservations(reservation_date, reservation_datetime, end_time):
    # checks for overlapping reservations for the new reseervation
    return Reservation.objects.filter(
        # get the new reservations date
        reservation_date = reservation_date,
        # check there is no reservation 2 hours away
        reservation_time__range=(
            reservation_datetime - timedelta(hours = 1, minutes = 45), # 2 hours before
            end_time, # 2 hours after
        )
    ).exists()

def generate_all_times():
    # Generate a list of times for the avaialble day
    return [
        reservation_datetime.replace(hour = h, minute = m)
            for h in range(10, 21)
            for m in range(0, 60, 15)
        ]

def filter_available_times():
    