from django.shortcuts import render

def my_account(request):
    return render(request, 'profiles/my_account.html')