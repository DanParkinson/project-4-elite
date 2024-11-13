from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


@login_required
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

def delete_account(request):
    if request.method == 'POST':
        user = request.User
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')
    return render(request, 'profiles/delete_account.html')
