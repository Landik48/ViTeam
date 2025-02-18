# Generated by Django 5.0.4 on 2024-04-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_users_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.IntegerField(verbose_name='Отряд')),
                ('scores_team', models.IntegerField(verbose_name='Баллы отряда')),
            ],
            options={
                'verbose_name_plural': 'Список отрядов',
            },
        ),
        migrations.RemoveField(
            model_name='users',
            name='auth_flag',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='scores',
        ),
        migrations.AddField(
            model_name='users',
            name='scores_personal',
            field=models.IntegerField(default=0, verbose_name='Личный рейтинг'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='scores_team',
            field=models.IntegerField(default=0, verbose_name='Баллы отряда'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='theme',
            field=models.TextField(default='gdh', verbose_name='Тема лагеря'),
            preserve_default=False,
        ),
    ]
