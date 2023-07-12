from django.db import models


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
    in_process = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f"{self.point_from} ➡ {self.point_to}"

    class Meta:
        verbose_name = "Поездка"
        verbose_name_plural = "Поездки"
