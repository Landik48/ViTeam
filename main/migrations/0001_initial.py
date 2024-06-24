# Generated by Django 5.0.4 on 2024-04-18 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='ФИО')),
                ('password', models.TextField(verbose_name='Пароль')),
                ('scores', models.IntegerField(verbose_name='Баллы')),
                ('auth_flag', models.BooleanField(default=False, verbose_name='Флаг авторизации')),
                ('tg_userid', models.IntegerField(verbose_name='Id телеграм')),
            ],
            options={
                'verbose_name_plural': 'Гости лагеря',
            },
        ),
    ]
