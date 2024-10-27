from django.shortcuts import render

# Create your views here.
def make_reservation(request):
    # Your reservation logic here
    return render(request, 'reservations/make_reservation.html')