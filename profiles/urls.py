from django.urls import path
from . import views

urlpatterns = [
    path('my-account/', views.my_account, name='my_account'),
    path('update-account/', views.update_account, name='update_account'),
    path('delete-account/', views.delete_account, name='delete_account'),
]