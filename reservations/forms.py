from django import forms
from .models import Reservation
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone_number','number_of_guests','reservation_date','reservation_time','special_occasion']
    
    name = forms.CharField(max_length=100, label='Name')
    
    number_of_guests = forms.IntegerField(
        min_value=1,
        max_value=8,
        label = 'Number Of Guests',
    )

    today = timezone.now().date()
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date',
            'min': today, #sets the minimum value to today
        }),
        label = 'Date'
    )

    TIME_CHOICES = [
        (f"{hour:02}:{minute:02}", f"{hour:02}:{minute:02}")
        for hour in range(10,21) # working hours are from 10 - 9 
        for minute in (0, 15, 30, 45) # reservation times every 15 minutes
    ]
    reservation_time = forms.ChoiceField(
        choices= TIME_CHOICES, # limits users to select open hours 
        label = 'Time',
    )

    special_occasion = forms.CharField(
        max_length=200,
        required=False,
        label='Special Occasion'
    )

    # combing date and time into one variable to stop users choosing a time in the past 
    # if their reservation is today
    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_time = cleaned_data.get('reservation_time')
    
        if reservation_date and reservation_time:
            # combine date and time into datetime
            reservation_datetime = timezone.make_aware(
                datetime.combine(
                reservation_date,
                datetime.strptime(reservation_time, "%H:%M").time()
                )
            )

            # If selected datetime is in the past throw an error
            if reservation_datetime < timezone.now():
                raise ValidationError("That time is in the past")
    
        return cleaned_data
        



        