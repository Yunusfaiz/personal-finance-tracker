from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            return render(request, 'registration/profile.html', {
                'message': 'Logged in successfully'
            })
        else:
            print("login failed")
            return render(request, 'registration/login.html', {
                'message': "Wrong credentials try again"
            })
    else:
        return render(request, "registration/login.html", {
            'message': "Error occured please try again"
        })


def profile(request):
    return render(request, "registration/profile.html")


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password != password2:
            return render(request, 'registration/register.html', {
                'error_message': "passwords don't match"
            })
        
        elif User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'registration/register.html', {
                'error_message': "Username or email already exists"
            })
        
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()

            return render(request, 'registration/login.html', {
                'message': 'User created!'
            })
    
    else:
        return render(request, "registration/register.html")