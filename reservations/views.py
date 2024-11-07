from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Reservation
from .forms import ReservationForm

@login_required
def make_reservation(request):
    """
    allows users to make reservations 
    uses submit a reservation date and reservation time
    these are combined into a reswervation datetime object
    checks for overlapping reservation times 
    if reservation time is taken. return list of available times
    """
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
                # If available times tell the user the 3 nearest times either side of chosen time
                if available_times:
                    # only shows three times either side of reservation time
                    available_times = get_available_times_slice(available_times, reservation_time)
                    # Inform the user that their chosen time is unavailable
                    form.add_error(None, "The chosen time is unavailable. Please see the nearest available times below:")
                else:
                    form.add_error(None, "There are no available times for this date")
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
    """
    Helper function to check for any overlapping reservations on the selected date.
    Returns True if an overlapping reservation is found, otherwise False.
    """
    return Reservation.objects.filter(
        reservation_date = reservation_date,
         # Look for existing reservations within the 1 hour 45 minute buffer range
        reservation_time__range=(
            reservation_datetime - timedelta(hours = 1, minutes = 45), # 2 hours before
            end_time, # 2 hours after
        )
    ).exists()

def generate_all_times(reservation_datetime):
    """
    Helper function to generate a list of all potential reservation times
    within the restaurant's open hours, starting every 15 minutes.
    """
    return [
        reservation_datetime.replace(hour = h, minute = m)
            for h in range(10, 21)
            for m in range(0, 60, 15)
        ]

def filter_available_times(all_times, reservation_date):
    """
    Helper function to filter out times that overlap with existing reservations on the selected date.
    Returns a list of available times that respect the 1 hour 45 minute buffer.
    """
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

def get_available_times_slice(available_times, reservation_time):
    """
    slice the avaible times so that only 3 either side of reservation_time are returned
    available times contains all the unbooked time slots
    add the reservation time to available times then select the nearest 3 reservations either side 
    remove the reservation time as this is unavailable
    return slice of nearest avaialbe times
    """
    # adds chosen reservation time to avaiable times
    available_times.append(reservation_time)
    # sorts the available times
    available_times.sort()
    # create index out of available times
    selected_time_index = available_times.index(reservation_time)
    # 3 times before and 3 times after chosen time
    start_index = max(0, selected_time_index - 3)
    end_index = min(len(available_times), selected_time_index + 3)
    # remove the reservation time as this is already booked
    available_times.remove(reservation_time)        
    # slice that shows three times either side reservation time
    return available_times[start_index:end_index]

# End of make reservations

@login_required
def my_reservations(request):
    """
    Generates a list of reservations made by the logged in user
    removes any reservation that is in the past
    """
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
    """
    requests the reservation information from the database 
    prepopulates the form 
    functions very similar to make reservations
    """
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
                # If available times tell the user the 3 nearest times either side of chosen time
                if available_times:
                    # only shows three times either side of reservation time
                    available_times = get_available_times_slice(available_times, new_time)
                    # Inform the user that their chosen time is unavailable
                    form.add_error(None, "The chosen time is unavailable. Please see the nearest available times below:")
                else:
                    form.add_error(None, "There are no available times for this date")
            else:
                form.save()
                return redirect('my_reservations')
    else:
        # prepopulate the forms information if not post
        form = ReservationForm(instance = reservation)
        # convert time field into a string for ChoiceField for prepopulating the form
        # this dosent work 
        if reservation.reservation_time:
            reservation_time_str = reservation.reservation_time.strftime("%H:%M")
            form.fields['reservation_time'].initial = reservation_time_str

    return render(request, 'reservations/edit_reservation.html',{
        'form' : form,
        'available_times' : available_times,
        'reservation' : reservation,
    })

@login_required
def delete_reservation(request, reservation_id):
    """
    get the reservation information or return 404 if not found
    deletes the reservation from the database
    """
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
def admin_reservation_overview(request):
    """
    function for admins to see a selected dates reservations
    pre load a reservations list. Date set to None as default
    """ 
    reservations = []
    selected_date = None
    if request.method == 'POST':
        selected_date = request.POST.get('reservation_date')
        if selected_date:
            #filter all of the selected dates reservations
            reservations = Reservation.objects.filter(
                reservation_date = selected_date
            ).order_by(
                'reservation_date', 'reservation_time')
    return render(request, 'reservations/admin_reservation_overview.html', {
        'reservations' : reservations,
        'selected_date' : selected_date,
    })

