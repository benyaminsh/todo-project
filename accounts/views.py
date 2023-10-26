from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                **form.cleaned_data
            )
            messages.success(request, 'User registerd successfully', 'success')
            return redirect('home')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', context={'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully', 'success')
                return redirect('home')

            else:
                messages.error(request, 'username or password is wrong', 'danger')
                return redirect('user_login')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', context={'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logged out is successfully')
    return redirect('home')
