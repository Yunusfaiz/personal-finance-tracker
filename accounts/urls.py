from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path("login_user", views.login_user, name='login_user'),
    path("profile", views.profile, name='profile'),
    path("register", views.register, name='register')
]