from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите почту"
    )
    avatar = models.ImageField(upload_to="avatar/", verbose_name="Аватар")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    country = models.CharField(max_length=100, verbose_name="страна")
    token = models.TextField(verbose_name="Токен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"