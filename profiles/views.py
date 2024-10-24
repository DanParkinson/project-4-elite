from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # Users must be logged on to access this view
def my_account(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email
    }
    return render(request, 'profiles/my_account.html', context)
