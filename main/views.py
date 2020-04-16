from django.shortcuts import render
from main.models import Car, Faq


# Create your views here.


def index(request):
    cars_i = Car.objects.all().filter(hot=True, isHidden=False)
    ctx = {'cars_i': cars_i}
    return render(request, 'index.html', ctx)


def about(request):
    faq = Faq.objects.all()
    ctx = {'faq': faq}
    return render(request, 'about.html', ctx)


def cars(request):
    all_cars = Car.objects.all().filter(isHidden=False)

    ctx = {'all_cars': all_cars}
    return render(request, 'cars.html', ctx)


def contact(request):
    ctx = {}
    return render(request, 'contact.html', ctx)


def services(request):
    ctx = {}
    return render(request, 'services.html', ctx)


def offer(request):
    ctx = {}
    return render(request, 'offer.html', ctx)



def car_details(request, id):
    cars_k = Car.objects.get(pk=id)
    price = "{:,}".format(cars_k.price)
    mileage = "{:,}".format(cars_k.mileage)
    ctx = {
        'cars': cars_k,
        'mileage': mileage,
        'price': price
    }
    return render(request, 'car_details.html', ctx)
