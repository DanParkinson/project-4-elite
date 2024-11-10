from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'), # loads index.html
    path('about-us/', views.about_us, name='about_us'),  # About Us page
    path('menu/', views.menu, name-'menu'),
]