from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    conversations = [
        ("LC", "Люблю поболтать!"),
        ('IC', "Не прочь поболтать, если мне комфортно"),
        ('NC', "Я скорее тихоня"),
        ]
    music = [
        ('LM', 'Включайте и погромче!'),
        ('IM', 'Все зависит от настроения - могу и спеть!'),
        ('NM', 'Предпочитаю тишину'),
        ]
    smoke = [
        ('LS', 'Я не против, если кто-то закурит'),
        ('IS', 'Можно курить, но не в машине'),
        ('NS', 'В моей машине не курят'),
    ]
    animals = [
        ('LA', 'Обожаю животных!'),
        ('IA', 'Зависит от животного'),
        ('NA', 'Предпочитаю поездки без животных'),
    ]
    profile_photo = models.ImageField(upload_to='upload_to/profile_photos', blank=True, default='user.png',
                              verbose_name="Изображение")
    prefer_conversations = models.CharField(max_length=2, choices=conversations, default='IC')
    prefer_music = models.CharField(max_length=2, choices=music, default='IM')
    prefer_smoke = models.CharField(max_length=2, choices=smoke, default='IS')
    prefer_animals = models.CharField(max_length=2, choices=animals, default='IA')
    base_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь",
                             related_name="user_profile")

    def __str__(self):
        return f"{self.base_user.username}"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
