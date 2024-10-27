from django.shortcuts import render
from reservations.models import Reservation
from django.utils import timezone
from datetime import datetime

# shows a users next reservation on the homepage
def index(request):
    next_reservation = None # for users without a reservation
    if request.user.is_authenticated: # check if logged in
        now = timezone.now() # current date and time

        # future reservations are filitered by two queries
        # first is for dates in the future
        # second is todays date with time in the future
        future_reservations = Reservation.objects.filter(
            user = request.user
        ).filter(
            reservation_date__gt = now.date() # future date reservations
        ) | Reservation.objects.filter(
            user = request.user,
            reservation_date = now.date(),
            reservation_time__gt = now.time(), # todays date with a future time
        )
        # next reservation is the next reservation as past
        # reservations have been filtered out
        next_reservation = future_reservations.order_by('reservation_date', 'reservation_time').first()

    return render(request, 'index.html', {'next_reservation' : next_reservation}) # loads index.html on request


def about_us(request):
    return render(request, 'about_us.html') # loads about_us.html on request