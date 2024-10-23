from django.shortcuts import render

def index(request):
    return render(request, 'index.html') # loads index.html on request

def about_us(request):
    return render(request, 'about_us.html') # loads index.html on request