# Generated by Django 5.1.1 on 2024-09-24 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Бар')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Ссылка')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('opening_year', models.IntegerField(verbose_name='Год открытия')),
            ],
            options={
                'verbose_name': 'бар',
                'verbose_name_plural': 'Бары',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Ссылка(уникальная)')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'теги',
                'verbose_name_plural': 'Тег',
            },
        ),
        migrations.CreateModel(
            name='BarDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setofshots.bar')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_dish_id', models.IntegerField(unique=True, verbose_name='ID позиции(уникальный')),
                ('title', models.CharField(max_length=32, verbose_name='Позиция меню')),
                ('slug', models.SlugField(max_length=32, unique=True, verbose_name='Ссылка')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('bars', models.ManyToManyField(through='app_setofshots.BarDish', to='app_setofshots.bar', verbose_name='Позиции меню')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='app_setofshots.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'позиция меню',
                'verbose_name_plural': 'Позиции меню',
            },
        ),
        migrations.AddField(
            model_name='bardish',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setofshots.dish'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Ивент')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='Ссылка')),
                ('start', models.DateTimeField(verbose_name='Дата и время')),
                ('status', models.CharField(choices=[('Not started yet', 'Ещё не началось'), ('Already started', 'Уже началось'), ('Ended', 'Закончилось')], max_length=15, verbose_name='Название')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ivents', to='app_setofshots.bar', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'ивенты',
                'verbose_name_plural': 'Ивент',
            },
        ),
        migrations.CreateModel(
            name='TagDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setofshots.dish')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setofshots.tag')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='tags',
            field=models.ManyToManyField(through='app_setofshots.TagDish', to='app_setofshots.tag', verbose_name='Теги'),
        ),
    ]