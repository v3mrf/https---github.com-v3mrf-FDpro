from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'nanies.html')

def services(request):
    return render(request, 'Reviews.html')

def contact(request):
    return render(request, 'Contact Us.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')