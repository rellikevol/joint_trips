from django.db import models
from django.contrib.auth.models import User
# Create your models here.

profile_conversations = [
    ("LC", "Люблю поболтать!"),
    ('IC', "Не прочь поболтать, если мне комфортно"),
    ('NC', "Я скорее тихоня"),
]
profile_music = [
    ('LM', 'Включайте и погромче!'),
    ('IM', 'Все зависит от настроения - могу и спеть!'),
    ('NM', 'Предпочитаю тишину'),
]
profile_smoke = [
    ('LS', 'Я не против, если кто-то закурит'),
    ('IS', 'Можно курить, но не в машине'),
    ('NS', 'В моей машине не курят'),
]
profile_animals = [
    ('LA', 'Обожаю животных!'),
    ('IA', 'Зависит от животного'),
    ('NA', 'Предпочитаю поездки без животных'),
]
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='upload_to/profile_photos', blank=True, default='user.png',
                              verbose_name="Изображение")
    prefer_conversations = models.CharField(max_length=2, choices=profile_conversations, default='IC')
    prefer_music = models.CharField(max_length=2, choices=profile_music, default='IM')
    prefer_smoke = models.CharField(max_length=2, choices=profile_smoke, default='IS')
    prefer_animals = models.CharField(max_length=2, choices=profile_animals, default='IA')
    base_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь",
                             related_name="user_profile")


    def __str__(self):
        return f"{self.base_user.username}"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
