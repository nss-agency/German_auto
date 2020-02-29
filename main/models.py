from django.db import models


# Create your models here.


class Car(models.Model):
    title = models.TextField('Назва',max_length=500)
    state = models.CharField('Стан',max_length=225, choices=(('Нова', 'Нова'), ('Підтримана (Б/У)', 'Підтримана (Б/У)')))
    first_register = models.IntegerField('Перша реєстрація')
    transmision = models.CharField('Коробка передач',max_length=225,
                                   choices=(('Автомат', 'Автомат'), ('Manual', 'Механіка'), ('Robot', 'Роботична')))
    mileage = models.IntegerField('Пробіг')
    power = models.IntegerField('Потужність')
    value = models.IntegerField('Об\'єм')
    color = models.CharField('Колір',max_length=225)
    salon = models.CharField('Салон',max_length=225, choices=(
        ('Fabric', 'Тканина'), ('Skin', 'Шкіра'), ('Skin/Alkantara', 'Шкіра/Альткантара')))
    parktronick = models.CharField('Парктронік',max_length=225, choices=(
        ('Nothing', 'Відсутні'), ('Front', 'Передні'), ('Back', 'Задні'), ('Front and Back', 'Передні та Задні'),('Camera', 'Камера')))
    category = models.CharField('Категорія',max_length=225, choices=(
        ('Sedan', 'Седан'), ('Universal', 'Універсал'), ('Crossover', 'Кросовер'), ('Hatchback', 'Хетчбек'),
        ('Passenger van', 'Легковий фургон'), ('Special tech', 'Спец техніка')))
    sity_flowrate = models.FloatField('Розхід по місту')
    trace_flowrate = models.FloatField('Розхід по шосе')
    mixed_flowrate = models.FloatField('Змішаний розхід')
    detail = models.TextField('Детальніше')

    isHidden = models.BooleanField('Приховати публікацію',
                                   default=False,
                                   help_text="Поставте галочку для того что <b>приховати</b> цей автомобіль у списку")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'
