from django.urls import path
from . import views

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('update-account/', views.update_account, name='update_account'),
    path('update-password/', views.update_password, name='update_password'),
]