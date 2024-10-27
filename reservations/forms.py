from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone_number','number_of_guests','reservation_date','reservation_time','special_occasion']
        