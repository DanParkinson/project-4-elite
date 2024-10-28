from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
@login_required
def make_reservation(request):
    if request.method == 'POST': # If submitting a form
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

            # checking if the new reservation overlaps with any reservations that already exist
            # If it exists then create overlapping_reservation variable
            overlapping_reservation = Reservation.objects.filter(
                # get the new reservations date
                reservation_date = reservation_date,
                # check there is no reservation 2 hours away
                reservation_time__range=(
                    reservation_datetime - timedelta(hours=1, minutes=45),  # 2 hours before
                    end_time  # 2 hours after
                )
            )

            # check is the overlapping reservation exists
            # new reservation is not saved and error is thrown
            if overlapping_reservation.exists():
                form.add_error(None, "This reservation is unavaiable")
            else:
                # new reservation is okay and is saved
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                return redirect('home')
    else:
        form = ReservationForm() # If loading the page, load the form
    return render(request, 'reservations/make_reservation.html', {'form': form})