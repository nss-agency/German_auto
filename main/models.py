from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.


class Car(models.Model):
    STATE_CHOICES = (
        ('Нова', 'Нова'),
        ('Потримана (Б/У)', 'Потримана (Б/У)')
    )
    TRANSMISION_CHOICES = (
        ('Автомат', 'Автомат'),
        ('Механіка', 'Механіка'),
        ('Роботична', 'Роботична'),
        ('Варіатор', 'Варіатор')
    )

    SALON_CHOICES = (
        ('Тканина', 'Тканина'),
        ('Шкіра', 'Шкіра'),
        ('Шкіра/Альткантара', 'Шкіра/Альткантара')
    )

    PARKTRONICK_CHOICES = (
        ('Відсутні', 'Відсутні'),
        ('Передні', 'Передні'),
        ('Задні', 'Задні'),
        ('Задні + Камера', 'Задні + Камера'),
        ('Передні та Задні', 'Передні та Задні'),
        ('Передні та Задні + Камера', 'Передні та Задні + Камера'),
        ('Камера', 'Камера')
    )

    CATEGORY_CHOICES = (
        ('Седан', 'Седан'),
        ('Універсал', 'Універсал'),
        ('Кросовер', 'Кросовер'),
        ('Хетчбек', 'Хетчбек'),
        ('Легковий фургон', 'Легковий фургон'),
        ('Спец техніка', 'Спец техніка')
    )

    PATROL_CHOICES = (
        ('Бензин', 'Бензин'),
        ('Дизель', 'Дизель'),
        ('Бензин/Газ', 'Бензин/Газ'),
        ('Електрика', 'Електрика'),
        ('Гібрид', 'Гібрид')
    )

    CURRENCY_CHOICES = (
        ('€', '€'),
        ('$', '$'),
        ('₴', '₴')
    )

    title = models.TextField('Назва', max_length=500)
    image = models.ImageField(upload_to='cars')
    state = models.CharField('Стан', max_length=225, choices=STATE_CHOICES)
    patrol = models.CharField('Тип Палива', max_length=225, choices=PATROL_CHOICES)
    first_register = models.CharField('Перша реєстрація', max_length=10)
    transmision = models.CharField('Коробка передач', max_length=225, choices=TRANSMISION_CHOICES)
    mileage = models.IntegerField('Пробіг')
    hp = models.PositiveIntegerField('Кількість кінських сил')
    value = models.FloatField('Об\'єм')
    color = models.CharField('Колір', max_length=225)
    salon = models.CharField('Салон', max_length=225, choices=SALON_CHOICES)
    parktronick = models.CharField('Парктронік', max_length=225, choices=PARKTRONICK_CHOICES)
    category = models.CharField('Категорія', max_length=225, choices=CATEGORY_CHOICES)
    sity_flowrate = models.FloatField('Розхід по місту')
    trace_flowrate = models.FloatField('Розхід по шосе')
    mixed_flowrate = models.FloatField('Змішаний розхід')
    detail = models.TextField('Детальніше')
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=0)
    currency = models.CharField('Ціна', max_length=2, default='€', choices=CURRENCY_CHOICES)

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


class Faq(models.Model):
    question = models.CharField('Питання', max_length=225)
    answer = models.TextField('Відповідь')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'


class Photo(models.Model):
    image = models.ImageField('Зображення',
                              upload_to='img',
                              null=True,
                              blank=True,
                              help_text='Зображення буде відображатись на слайдері головної сторінки')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)


@receiver(post_delete)
def submission_delete(sender, instance, **kwargs):
    try:
        instance.image.delete(False)
    except AttributeError:
        pass
