from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home),

    path('about/', views.about, name='about'),
    path('nanies.html', views.about),

    path('services/', views.services, name='services'),
    path('Reviews.html', views.services),

    path('contact/', views.contact, name='contact'),
    path('Contact Us.html', views.contact),

    path('login/', views.login_page, name='login'),
    path('login.html', views.login_page),

    path('register/', views.register_page, name='register'),
    path('register.html', views.register_page),
]