from django.urls import path
from . import views

urlpatterns = [
    path('make-reservation/', views.make_reservation, name='make_reservation'),
]