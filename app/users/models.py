"""Подсказка.
При использовании `postgres` модели `IP` и `Agent`
можно исключить, добавив соответствующие поля в `MyUser`.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    username = models.CharField(
        verbose_name='Уникальный юзернейм',
        max_length=20,
        unique=True,
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=20,
    )

    def __str__(self):
        return f'{self.username}: {self.email}'

    def password_change(self, request, extra_context=None):
        raise ValueError


class IP(models.Model):
    ip = models.GenericIPAddressField(
        verbose_name='IP пользователя'
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=MyUser,
        on_delete=models.CASCADE,
        related_name='ips'
    )

    class Meta:
        unique_together = (('ip', 'user'),)


class Agent(models.Model):
    agent = models.CharField(
        verbose_name='Устройство пользователя',
        max_length=100
    )
    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=MyUser,
        on_delete=models.CASCADE,
        related_name='agents'
    )

    class Meta:
        unique_together = (('agent', 'user'),)
