from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(region="GB")
    number_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_occasion = models.CharField(max_length=400, blank=True)
    seat_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.reservation_date} {self.reservation_time} (Table {self.seat_id})"
