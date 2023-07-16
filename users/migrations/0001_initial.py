# Generated by Django 4.2.3 on 2023-07-16 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, default='user.png', upload_to='upload_to/profile_photos', verbose_name='Изображение')),
                ('prefer_conversations', models.CharField(choices=[('LC', 'Люблю поболтать!'), ('IC', 'Не прочь поболтать, если мне комфортно'), ('NC', 'Я скорее тихоня')], default='IC', max_length=2)),
                ('prefer_music', models.CharField(choices=[('LM', 'Включайте и погромче!'), ('IC', 'Все зависит от настроения - могу и спеть!'), ('NM', 'Предпочитаю тишину')], default='IM', max_length=2)),
                ('prefer_smoke', models.CharField(choices=[('LS', 'Я не против, если кто-то закурит'), ('IS', 'Можно курить, но не в машине'), ('NS', 'В моей машине не курят')], default='IS', max_length=2)),
                ('prefer_animals', models.CharField(choices=[('LA', 'Обожаю животных!'), ('IS', 'Зависит от животного'), ('NS', 'Предпочитаю поездки без животных')], default='IA', max_length=2)),
                ('base_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
