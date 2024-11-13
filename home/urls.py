from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('menu/', views.menu, name='menu'),
]