from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "finance/dashboard.html")


def transaction_list(request):
    return render(request, "finance/transaction_list.html")


def transaction_form(request):
    return render(request, "finance/transaction_form.html")


def category_list(request):
    return render(request, "finance/category_list.html")


def category_form(request):
    return render(request, "finance/category_form.html")
