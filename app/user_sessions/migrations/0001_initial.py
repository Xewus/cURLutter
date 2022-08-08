# Generated by Django 4.1 on 2022-08-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='session key')),
                ('session_data', models.TextField(verbose_name='session data')),
                ('expire_date', models.DateTimeField(db_index=True, verbose_name='expire date')),
                ('user_id', models.IntegerField(db_index=True, null=True, verbose_name='id пользователя')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
                'abstract': False,
            },
        ),
    ]