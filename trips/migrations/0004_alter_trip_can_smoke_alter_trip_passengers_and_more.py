# Generated by Django 4.2.3 on 2023-07-17 09:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0003_alter_trip_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='can_smoke',
            field=models.CharField(choices=[('LS', 'Можно курить'), ('IS', 'Можно курить, но не в машине'), ('NS', 'Курить нельзя')], default='IS', max_length=2, verbose_name='Можно ли курить'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='passengers',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_passengers', to=settings.AUTH_USER_MODEL, verbose_name='Пассажиры'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='with_animals',
            field=models.CharField(choices=[('LA', 'Можно с животными'), ('IA', 'Наличие животных обсуждаемо'), ('NA', 'Без животных')], default='IA', max_length=2, verbose_name='Можно ли с животными'),
        ),
    ]