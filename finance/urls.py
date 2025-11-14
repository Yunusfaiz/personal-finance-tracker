from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name='dashboard'),
    path("transaction_list", views.transaction_list, name='transaction_list'),
    path("transaction_form", views.transaction_form, name='transaction_form'),
    path("category_list", views.category_list, name='category_list'),
    path("category_form", views.category_form, name='category_form')
]