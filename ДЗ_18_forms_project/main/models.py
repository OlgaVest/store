
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Модель профиля пользователя для хранения дополнительной информации.
    Связана с встроенной моделью User через OneToOneField.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")
    bio = models.TextField(max_length=500, blank=True, verbose_name="Биография")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Сигнал: Создает профиль при создании нового пользователя.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Сигнал: Сохраняет профиль при сохранении пользователя.
    """
    instance.profile.save()
