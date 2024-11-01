from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Reservation
from .forms import ReservationForm

@login_required
def make_reservation(request):
    # empty list to store available times if reservation time is already booked
    available_times = []

    # Process the form submission
    if request.method == 'POST': 
        form = ReservationForm(request.POST)
        if form.is_valid():

            # Extract and clean the reservation date and time from the form
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            # Combine date and time into a timezone-aware datetime object
            reservation_datetime = timezone.make_aware(
                datetime.combine(
                reservation_date,
                datetime.strptime(reservation_time, "%H:%M").time()
                ))
            # Set the reservation end time to enforce a 1 hour 45 minute buffer
            end_time = reservation_datetime + timedelta(hours=1, minutes=45)

            # Check for overlapping reservations within the buffer period
            if check_overlapping_reservations(reservation_date, reservation_datetime, end_time):
                # Generate all possible times for the restaurant's open hours on the selected day
                all_times = generate_all_times(reservation_datetime)
                # Filter available times by removing those that overlap with existing reservations
                available_times = filter_available_times(all_times, reservation_date)

                # If no available times, add an error message for the user
                if not available_times:
                    form.add_error(None, "There are no available times for this date")
                else:
                    # Inform the user that their chosen time is unavailable
                    form.add_error(None, "The chosen time is unavailable. Please see the available times below:")

            else:
                # If no overlaps are found, save the reservation and associate it with the current user
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                return redirect('home')

    # if request method else
    else:
        form = ReservationForm()
    # Render the reservation form template with the form and available times (if any)
    return render(request, 'reservations/make_reservation.html', {'form': form, 'available_times': available_times})

def check_overlapping_reservations(reservation_date, reservation_datetime, end_time):
    # Helper function to check for any overlapping reservations on the selected date.
    # Returns True if an overlapping reservation is found, otherwise False.
    return Reservation.objects.filter(
        reservation_date = reservation_date,
         # Look for existing reservations within the 1 hour 45 minute buffer range
        reservation_time__range=(
            reservation_datetime - timedelta(hours = 1, minutes = 45), # 2 hours before
            end_time, # 2 hours after
        )
    ).exists()

def generate_all_times(reservation_datetime):
    # Helper function to generate a list of all potential reservation times
    # within the restaurant's open hours, starting every 15 minutes.
    return [
        reservation_datetime.replace(hour = h, minute = m)
            for h in range(10, 21)
            for m in range(0, 60, 15)
        ]

def filter_available_times(all_times, reservation_date):
    # Helper function to filter out times that overlap with existing reservations on the selected date.
    # Returns a list of available times that respect the 1 hour 45 minute buffer.
    available_times = []
    # get all reservations on the chosen date
    chosen_day_reservations = Reservation.objects.filter(
        reservation_date = reservation_date
        )
    
    
    # Check each potential reservation time for conflicts
    for time in all_times:
        # ignores times in the past if todays date
        if reservation_date ==  timezone.now().date() and time < timezone.now():
            continue
        # If no overlapping reservation exists within the buffer, add time to available_times
        if not chosen_day_reservations.filter(
            reservation_time__range = (
                time - timedelta(hours=1, minutes=45),
                time + timedelta(hours=1, minutes=45),
            )
        ).exists():
            available_times.append(time.strftime("%H:%M"))
    # returns list that contains all times that arent taken
    return available_times

# End of make reservations

@login_required
def my_reservations(request):
    # get the current time
    now = timezone.now()

    # filter reservations to collect the logged in users reservations
    my_reservations = Reservation.objects.filter(
        user=request.user, 
        reservation_date__gte = now.date() # filter out previous days
        ).exclude(
            # excludes reservations on todays date that time is in the past
            reservation_date = now.date(),
            reservation_time__lt = now.time(),
        ).order_by(
            'reservation_date', 'reservation_time')
    
    # Pass reservations to the template
    return render(request, 'reservations/my_reservations.html', {'reservations': my_reservations})

@login_required
def edit_reservation(request, reservation_id):
    # get the reservation information or return 404 if not found
    reservation = get_object_or_404(
        Reservation,
        id = reservation_id,
        user = request.user,
    )

    # empty list to store available times if reservation time is already booked
    available_times = []

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            # Extract new reservation details from form
            new_date= form.cleaned_data['reservation_date']
            new_time= form.cleaned_data['reservation_time']
            new_guests= form.cleaned_data['number_of_guests']
        
            # create new datetime object
            new_datetime = timezone.make_aware(
                datetime.combine(
                new_date,
                datetime.strptime(new_time, "%H:%M").time()
                )
            )
            # Set the reservation end time to enforce a 1 hour 45 minute buffer
            end_time = new_datetime + timedelta(hours=1, minutes=45)

                    # Check for overlapping reservations within the buffer period
            if check_overlapping_reservations(new_date, new_datetime, end_time):
                # Generate all possible times for the restaurant's open hours on the selected day
                all_times = generate_all_times(new_datetime)
                # Filter available times by removing those that overlap with existing reservations
                available_times = filter_available_times(all_times, new_date)

                if not available_times:
                    form.add_error(None, "No available times for this date")
                else:
                    form.add_error(None, "Selected time is unavailable. See available times below.")
            else:
                form.save()
                return redirect('my_reservations')
    
    else:
        # prepopulate the forms information if not post
        form = ReservationForm(instance = reservation)
        # time field is not prepopulating in the form when requested
        # Reservation found: test - 2024-11-12 12:45:00 is the data format 
        # the time in the form is a choice field which requires a string? 
        # figure out how to fix that
    
    return render(request, 'reservations/edit_reservation.html',{
        'form' : form,
        'available_times' : available_times,
        'reservation' : reservation,
    })

def delete_reservation(request, reservation_id):
    # get the reservation information or return 404 if not found
    reservation = get_object_or_404(
        Reservation,
        id = reservation_id,
        user = request.user,
    )

    if request.method == 'POST':
        reservation.delete()
        return redirect('my_reservations')
    
    return render(request, 'reservations/delete_reservation.html', {'reservation' : reservation})

@staff_member_required
# function for admins to see a selected dates reservations
def view_reservations_by_date(request):
    # pre load a reservations list. Date et to None as default 
    reservations = []
    selected_date = None

    if request.method == 'POST':
        selected_date = request.POST.get('reservation_date')

        if selected_date:
            #filter all of the selected dates reservations
            reservations = Reservation.objects.filter(reservation_date = selected_date)
        
    return render(request, 'reservations/view_reservations_by_date.html', {
        'reservations' : reservations,
        'selected_date' : selected_date,
    })

