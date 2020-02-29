from django.shortcuts import render
from main.models import Car


# Create your views here.


def index(request):
    ctx = {'index': True}
    return render(request, 'index.html',ctx )


def about(request):
    ctx = {'about': True}
    return render(request, 'about.html', ctx)


def cars(request):
    ctx = {'cars': True}
    return render(request, 'cars.html',ctx)


def contact(request):
    ctx = {'contact': True}
    return render(request, 'contact.html',ctx)


def services(request):
    ctx = {'services': True}
    return render(request, 'services.html',ctx)


def offer(request):
    ctx = {'offer': True}
    return render(request, 'offer.html',ctx)


def car(request):
    cars_k = Car.objects.all()
    ctx = {'cars': cars_k}
    return render(request, 'car.html',ctx)
