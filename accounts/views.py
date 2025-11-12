from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse, include
# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            print("login success")
            return redirect('profile')
        else: 
            messages.error(request, 'Invalid username or password. Try again.')
            print("login failed")
            return redirect('login')
    else:
        return render(request, "registration/login.html", {})


def profile(request):
    return render(request, "registration/profile.html")


def register(request):
    return render(request, "registration/register.html")