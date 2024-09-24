from django.db.models import (
    Model,
    CharField, IntegerField, DateTimeField,
    ForeignKey, ManyToManyField, OneToOneField,
    ImageField, SlugField, ManyToOneRel,
    CASCADE,
)
from django.contrib.auth import get_user_model

from datetime import datetime

User = get_user_model()
CHOICES_STATUS = (
    ('Not started yet', 'Ещё не началось'),
    ('Already started', 'Уже началось'),
    ('Ended', 'Закончилось')
)


class Tag(Model):
    title = CharField(max_length=16, verbose_name='Название')

    class Meta:
        verbose_name = 'теги'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.title


class Category(Model):
    title = CharField(max_length=32, verbose_name='Название')
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка(уникальная)'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Event(Model):
    title = CharField(max_length=128, verbose_name='Ивент')
    description = CharField(max_length=1024, verbose_name='Описание')
    slug = SlugField(max_length=128, unique=True, verbose_name='Ссылка')
    start = DateTimeField(verbose_name='Дата и время')
    place = ForeignKey(
        to='Bar', related_name='ivents', on_delete=CASCADE,
        verbose_name='Место'
    )
    status = CharField(
        max_length=15, choices=CHOICES_STATUS, verbose_name='Название'
    )

    class Meta:
        verbose_name = 'ивенты'
        verbose_name_plural = 'Ивент'

    def __str__(self):
        return f'{self.title}, {self.start}, {self.status}.'


class Dish(Model):
    unique_dish_id = CharField(
        unique=True,
        verbose_name='Уникальный идентификатор [Рюмочная_Позиция]',
        max_length=64
    )
    title = CharField(max_length=32, verbose_name='Позиция меню')
    slug = SlugField(max_length=32, unique=True, verbose_name='Ссылка')
    category = ForeignKey(
        Category, on_delete=CASCADE,
        null=False, related_name='dishes', verbose_name='Категория'
    )
    description = CharField(max_length=1024, verbose_name='Описание')
    tags = ManyToManyField(Tag, through='TagDish', verbose_name='Теги')
    price = IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'позиция меню'
        verbose_name_plural = 'Позиции меню'

    def __str__(self):
        return self.title


class BarDish(Model):
    bar = ForeignKey('Bar', on_delete=CASCADE)
    dish = ForeignKey(Dish, on_delete=CASCADE)

    def __str__(self):
        return f'{self.bar} ==> {self.dish}'


class Bar(Model):
    title = CharField(max_length=32, verbose_name='Бар')
    slug = SlugField(max_length=32, unique=True, verbose_name='Ссылка')
    description = CharField(max_length=1024, verbose_name='Описание')
    address = CharField(max_length=128, verbose_name='Адрес')
    opening_year = IntegerField(verbose_name='Год открытия')
    dishes = ManyToManyField(
        to=Dish, through='BarDish',
        verbose_name='Позиции меню',
        blank=False
    )

    class Meta:
        verbose_name = 'бар'
        verbose_name_plural = 'Бары'

    def get_list(self):
        return BarDish.objects.all()

    def __str__(self):
        return self.title


class TagDish(Model):
    tag = ForeignKey(Tag, on_delete=CASCADE)
    dish = ForeignKey(Dish, on_delete=CASCADE)

    def __str__(self):
        return f'Теги для{self.dish}: {self.tag}'
