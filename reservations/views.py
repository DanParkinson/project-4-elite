from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Reservation
from .forms import ReservationForm

table_info = {
    #seat_id : capacity
    1 : 2,
    2 : 2,
    3 : 4,
    4 : 4,
    5 : 6,
    6 : 6,
    7 : 8,
    8 : 8,
}

@login_required
def make_reservation(request):
    """
    users can submit a form to make a reservation 
    if not submitting then retrieve the form
    """
    available_times = []
    suitable_tables = {}
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # get cleaned form data
            reservation_date = form.cleaned_data['reservation_date']
            reservation_time = form.cleaned_data['reservation_time']
            number_of_guests = form.cleaned_data['number_of_guests']

            # create a datetime object and an end time for reservations
            reservation_datetime = create_datetime_object(reservation_date, reservation_time)
            end_time = create_end_time(reservation_datetime)

            assigned_seat = None
            # selects the tables suitable for the party size
            suitable_tables = get_suitable_tables(number_of_guests, table_info)
            # generates all the available times for the day
            all_times = generate_all_times(reservation_datetime)

            # for each table, check if there are any reservations conflicitng with chosen reservation time
            # if no conflict, assign the seat_id
            for seat_id in suitable_tables.keys():
                # Only check tables that can fit the required number of guests
                    if not check_overlapping_reservation(seat_id, reservation_date, reservation_time, reservation_datetime, end_time):
                        assigned_seat = seat_id
                        break
            
            # save the form 
            if assigned_seat:
                reservation = form.save(commit=False)
                reservation.seat_id = assigned_seat
                reservation.user = request.user
                reservation.save()
                return redirect('home')
            else:
                
                # if time is invlaid, return a list of available times
                all_available_times = set() # set to remove duplicates
                for seat_id in suitable_tables.keys():
                    available_seat_times = filter_available_times(all_times, reservation_date, seat_id)
                    available_times_slice = get_available_times_slice(available_seat_times, reservation_time)
                    all_available_times.update(available_times_slice)

                # order available times and change to a list
                available_times = sorted(list(all_available_times))
                if available_times:
                    form.add_error(None, "The selected time is unavailable. Please choose from nearby available times.")
                else:
                    form.add_error(None, "There are no available tables on this date")

                return render(request, 'reservations/make_reservation.html', {
                    'form' : form,
                    'available_times': available_times,
                    'error_message': 'Sorry, no tables are available at that time. Please choose another time.'   
                })
    else:
        form = ReservationForm()

    return render(request, 'reservations/make_reservation.html', {'form': form})

def get_suitable_tables(number_of_guests, table_info):
    """
    return a dictionary of suitable tables to accomodate the number of guests
    """
    suitable_tables = {}
    for seat_id, capacity in table_info.items():
        if capacity >= number_of_guests:
            suitable_tables[seat_id] = capacity
    return suitable_tables
    
def create_datetime_object(reservation_date, reservation_time):
    """
    Combine date and time into a timezone-aware datetime object
    """
    reservation_datetime = timezone.make_aware(
        datetime.combine(
        reservation_date,
        datetime.strptime(reservation_time, "%H:%M").time()
    ))
    return reservation_datetime

def create_end_time(reservation_datetime):
    """
    Set the reservation end time to enforce a 45 minute buffer
    """
    end_time = reservation_datetime + timedelta(minutes=45)
    return end_time

def check_overlapping_reservation(seat_id, reservation_date, reservation_time, reservation_datetime, end_time):
    """
    Helper function to check for any overlapping reservations on the selected date.
    Returns True if an overlapping reservation exists
    """
    overlapping_reservation = Reservation.objects.filter(
        seat_id=seat_id,
        reservation_date = reservation_date,
        reservation_time__range=(
            reservation_datetime - timedelta(minutes=45),
            end_time
        )
    )
    return overlapping_reservation.exists()

def generate_all_times(reservation_datetime):
    """
    Helper function to generate a list of all potential reservation times
    within the restaurant's open hours, starting every 15 minutes.
    """
    all_times =  [
        reservation_datetime.replace(hour = h, minute = m)
            for h in range(10, 21)
            for m in range(0, 60, 15)
        ]
    return all_times

def filter_available_times(all_times, reservation_date, seat_id):
    """
    Helper function to filter out times that overlap with existing reservations on the selected date.
    Returns a list of available times that respect the 1 hour 45 minute buffer.
    """
    available_times = []
    # get all reservations on the chosen date
    seat_reservations = Reservation.objects.filter(
        reservation_date = reservation_date,
        seat_id=seat_id,
        )
    # Check each potential reservation time for conflicts
    for time in all_times:
        # ignores times in the past if todays date
        if reservation_date ==  timezone.now().date() and time < timezone.now():
            continue
        # If no overlapping reservation exists within the buffer, add time to available_times
        if seat_reservations.filter(
            reservation_time__range = (
                time - timedelta(minutes=45),
                time + timedelta(minutes=45),
            )
        ).exists():
            continue
        available_times.append(time.strftime("%H:%M"))

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
    # create index out of available times. Finds the position of the reservation time
    selected_time_index = available_times.index(reservation_time)
    # 3 times before and 3 times after reservation time 
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

            # create a datetime object and an end time for reservations
            new_datetime = create_datetime_object(new_date, new_time)
            end_time = create_end_time(new_datetime)

            assigned_seat = None
            # generates all the available times for the day
            all_times = generate_all_times(new_datetime)
            # selects the tables suitable for the party size
            suitable_tables = get_suitable_tables(new_guests, table_info)

            # for each table, check if there are any reservations conflicitng with chosen reservation time
            # if no conflict, assign the seat_id
            for seat_id in suitable_tables.keys():
                if not check_overlapping_reservation(seat_id, new_date, new_time, new_datetime, end_time):
                    assigned_seat = seat_id
                    break
                       # save the form 
            if assigned_seat:
                reservation = form.save(commit=False)
                reservation.seat_id = assigned_seat
                reservation.save()
                return redirect('my_reservations')
            else:
                
                # if time is invlaid, return a list of available times
                all_available_times = set() # set to remove duplicates
                for seat_id in suitable_tables.keys():
                    available_seat_times = filter_available_times(all_times, new_date, seat_id)
                    available_times_slice = get_available_times_slice(available_seat_times, new_time)
                    all_available_times.update(available_times_slice)

                # order available times and change to a list
                available_times = sorted(list(all_available_times))
                if available_times:
                    form.add_error(None, "The selected time is unavailable. Please choose from nearby available times.")
                else:
                    form.add_error(None, "There are no available tables on this date")

    else:
        #prepopulate the form if request
        form = ReservationForm(instance = reservation)

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

