from django.urls import path
from . import views

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),  # URL to access the account page
]