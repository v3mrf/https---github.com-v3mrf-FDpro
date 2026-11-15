from django.shortcuts import render

from .models import Service

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

from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ServiceForm


def service_list(request):
    services = Service.objects.prefetch_related(
        'servicedetail_set'
    ).all()

    return render(request, 'service_list.html', {
        'services': services
    })



@staff_member_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()

    return render(
        request,
        'add_service.html',
        {'form': form}
    )
