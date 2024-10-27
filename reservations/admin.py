from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone_number','number_of_guests','reservation_date','reservation_time','special_occasion')
