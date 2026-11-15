from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-service/', views.add_service, name='add_service'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    path('contact/', views.contact, name='contact'),

    path('login/', views.login_page, name='login'),

    path('register/', views.register_page, name='register'),

path('service-list/', views.service_list, name='service_list'),
]