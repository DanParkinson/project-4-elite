from django.shortcuts import render
from reservations.models import Reservation
from django.utils import timezone

def index(request):
    next_reservation = None # for users without a reservation
    if request.user.is_authenticated: # check if logged in
        next_reservation = Reservation.objects.filter(
            user = request.user, # get users reservations
            reservation_date__gte = timezone.now().date(), # get the future reservations
        ).order_by('reservation_date', 'reservation_time').first() # get the first reservation

    return render(request, 'index.html', {'next_reservation' : next_reservation}) # loads index.html on request

def about_us(request):
    return render(request, 'about_us.html') # loads about_us.html on request