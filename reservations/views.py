from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm

# Create your views here.
@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})