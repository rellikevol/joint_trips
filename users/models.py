from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image

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
    profile_photo = models.ImageField(upload_to='upload_to/profile_photos', blank=True, default='user.jpg',
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_photo.path)


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Отправитель",
                               related_name='sender')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Получатель",
                                  related_name='recipient')
    text = models.TextField(verbose_name='Сообщение')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender.base_user.username} to {self.recipient.base_user.username}' \
               f' at {self.date} {self.time}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Chat(models.Model):
    members = models.ManyToManyField(Profile, verbose_name="Участники")
    messages = models.ManyToManyField(Message, verbose_name='Сообщения', blank=True)

    def __str__(self):
        return f'Чат {self.pk}'

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
