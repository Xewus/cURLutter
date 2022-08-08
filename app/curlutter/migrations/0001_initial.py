# Generated by Django 4.1 on 2022-08-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.URLField(verbose_name='Оригинальная ссылка')),
                ('short', models.CharField(max_length=10, unique=True, verbose_name='Укороченная ссылка')),
                ('end_time', models.DateTimeField(null=True, verbose_name='Время окончания действия ссылки')),
            ],
        ),
    ]