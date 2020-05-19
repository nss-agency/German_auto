from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Car, Faq, Photo
from django.core.mail import send_mail
from .decorators import check_recaptcha


# Create your views here.

def send_contact(request):
    fname = request.POST.get('first_name', '')
    lname = request.POST.get('last_name', '')
    subject = 'Повідомлення з веб сайту'
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    whatsapp = request.POST.get('tel', '')
    messages = 'Ім\'я та Прізвище: {} {} \n' \
               'Номер Телефону: {}\n' \
               'Від кого(E-mail): {}\n' \
               'Повідомлення: \n{}\n\n\n\n' \
               'Надіслано з ' \
               '<a href="https://german-auto.in.ua/">german-auto.in.ua</a>'.format(fname, lname, whatsapp, from_email,
                                                                                   message)
    send_mail(subject, messages, 'noreply@german-auto.in.ua', ['henow32444@reqaxv.com'], fail_silently=False)


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



@check_recaptcha
def contact(request):
    ctx = {'success': False,
           'fail': False}
    if request.method == 'POST':
        if request.recaptcha_is_valid:
            send_contact(request)
            ctx['success'] = True
        else:
            ctx['fail'] = True
    return render(request, 'contact.html', ctx)


def services(request):
    ctx = {}
    return render(request, 'services.html', ctx)


def offer(request):
    ctx = {}
    return render(request, 'offer.html', ctx)


def car_details(request, id):
    cars_k = Car.objects.get(pk=id)
    gallery = Photo.objects.filter(car=cars_k)
    ctx = {
        'cars': cars_k,
        'gallery': gallery,
    }
    return render(request, 'car_details.html', ctx)
