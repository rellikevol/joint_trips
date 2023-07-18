from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

smoke = [
        ('LS', 'Можно курить'),
        ('IS', 'Можно курить, но не в машине'),
        ('NS', 'Курить нельзя'),
    ]
animals = [
        ('LA', 'Можно с животными'),
        ('IA', 'Наличие животных обсуждаемо'),
        ('NA', 'Без животных'),
    ]

class Trip(models.Model):
    locale_from = models.TextField(verbose_name='Населённый пункт откуда')
    point_from = models.TextField(verbose_name='Откуда')
    longitude_from = models.TextField(verbose_name='Долгота откуда')
    latitude_from = models.TextField(verbose_name='Широта откуда')
    locale_to = models.TextField(verbose_name='Населённый пункт куда')
    point_to = models.TextField(verbose_name='Куда')
    longitude_to = models.TextField(verbose_name='Долгота куда')
    latitude_to = models.TextField(verbose_name='Широта куда')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    spaces = models.IntegerField(verbose_name='Места')
    empty_spaces = models.IntegerField(verbose_name='Свободные места')
    #
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    # уже выехали
    in_process = models.BooleanField(default=False, verbose_name='Поездка а процессе')
    # уже приехали
    is_finished = models.BooleanField(default=False, verbose_name='Завершенная')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Водитель",
                              related_name="user_driver")
    passengers = models.ManyToManyField(Profile, blank=True, verbose_name="Пассажиры", related_name="user_passengers")
    can_smoke = models.CharField(max_length=2, choices=smoke, default='IS', verbose_name='Можно ли курить')
    with_animals = models.CharField(max_length=2, choices=animals, default='IA', verbose_name='Можно ли с животными')


    def __str__(self):
        return f"{self.point_from} ➡ {self.point_to}"

    class Meta:
        verbose_name = "Поездка"
        verbose_name_plural = "Поездки"
