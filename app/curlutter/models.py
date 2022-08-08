from django.db import models

from main import settings


class Link(models.Model):
    original = models.URLField(
        verbose_name='Оригинальная ссылка',
        null=False
    )
    short = models.CharField(
        verbose_name='Укороченная ссылка',
        max_length=settings.MAX_LEN_SHORT_URL,
        null=False,
        unique=True
    )
    end_time = models.DateTimeField(
        verbose_name='Время окончания действия ссылки',
        null=True
    )

    def __str__(self):
        return f'{self.short} -> {self.original[:33]}'
