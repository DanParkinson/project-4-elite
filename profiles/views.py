from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


@login_required # Users must be logged on to access this view
def my_account(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email
    }
    return render(request, 'profiles/my_account.html', context)


def update_account(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("my_account")
    else:
        form = UserUpdateForm(instance=request.user)
        
    return render(request, 'profiles/update_account.html', {'form': form})


def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)  # Important to keep the user logged in
            return redirect('my_account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request,  'profiles/update_password.html', {'form': form})