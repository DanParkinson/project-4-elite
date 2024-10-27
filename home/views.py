from django.shortcuts import render
from reservations.models import Reservation
from django.utils import timezone
from datetime import datetime

# shows a users next reservation on the homepage
def index(request):
    next_reservation = None # for users without a reservation
    if request.user.is_authenticated: # check if logged in
        now = timezone.now() # current date and time for removing reservations today that time has expired
        future_reservations = Reservation.objects.filter(user = request.user) # get users reservations

        # filter out past reservations
        for reservation in future_reservations:
            reservation_datetime = timezone.make_aware(
                datetime.combine(reservation.reservation_date, reservation.reservation_time)
            )
            # 
            if reservation_datetime >= now:
                next_reservation = reservation
                break # get the first valid future reservation

    return render(request, 'index.html', {'next_reservation' : next_reservation}) # loads index.html on request

def about_us(request):
    return render(request, 'about_us.html') # loads about_us.html on request