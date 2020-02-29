from django.db import models


# Create your models here.


class Car(models.Model):
    title = models.TextField('Назва', max_length=500)
    state = models.CharField('Стан', max_length=225,
                             choices=(('Нова', 'Нова'), ('Підтримана (Б/У)', 'Підтримана (Б/У)')))
    first_register = models.IntegerField('Перша реєстрація')
    transmision = models.CharField('Коробка передач', max_length=225,
                                   choices=(('Автомат', 'Автомат'), ('Механіка', 'Механіка'), ('Роботична', 'Роботична')))
    mileage = models.IntegerField('Пробіг')
    power = models.IntegerField('Потужність')
    value = models.IntegerField('Об\'єм')
    color = models.CharField('Колір', max_length=225)
    salon = models.CharField('Салон', max_length=225, choices=(
        ('Тканина', 'Тканина'), ('Шкіра', 'Шкіра'), ('Шкіра/Альткантара', 'Шкіра/Альткантара')))
    parktronick = models.CharField('Парктронік', max_length=225, choices=(
        ('Відсутні', 'Відсутні'), ('Передні', 'Передні'), ('Задні', 'Задні'), ('Передні та Задні', 'Передні та Задні'),
        ('Camera', 'Камера')))
    category = models.CharField('Категорія', max_length=225, choices=(
        ('Седан', 'Седан'), ('Універсал', 'Універсал'), ('Кросовер', 'Кросовер'), ('Хетчбек', 'Хетчбек'),
        ('Легковий фургон', 'Легковий фургон'), ('Спец техніка', 'Спец техніка')))
    sity_flowrate = models.FloatField('Розхід по місту')
    trace_flowrate = models.FloatField('Розхід по шосе')
    mixed_flowrate = models.FloatField('Змішаний розхід')
    detail = models.TextField('Детальніше')
    hot = models.BooleanField('Гаряча Пропозиція',
                              default=False,
                              help_text="Поставте галочку для того что <b>розмістити</b> цей автомобіль у списку "
                                        "горячих пропозицій")

    isHidden = models.BooleanField('Приховати публікацію',
                                   default=False,
                                   help_text="Поставте галочку для того что <b>приховати</b> цей автомобіль у списку")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'
