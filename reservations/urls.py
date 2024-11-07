from django.urls import path
from . import views

urlpatterns = [
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('view-reservations/', views.admin_reservation_overview, name='admin_reservation_overview'),
]