from datetime import timedelta

from django.db.models import (
    Model,
    CharField, IntegerField,
    ForeignKey, ManyToManyField,
    ImageField, SlugField, BooleanField,
    CASCADE, TextField, DateField, DateTimeField,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe, escape

User = get_user_model()


class Tag(Model):
    title = CharField(max_length=16, verbose_name='Название')
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

    class Meta:
        verbose_name = 'теги'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.title


class Category(Model):
    title = CharField(max_length=32, verbose_name='Название')
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка(уникальная)',
        help_text='Можно оставить пустым', blank=True,
    )
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Event(Model):
    title = CharField(max_length=128, verbose_name='Ивент')
    description = TextField(
        max_length=1024,
        verbose_name='Описание',
        help_text=f'Для вставки красивых ссылок(чтобы можно было кликать '
                  'на слово)\nследует использовать шаблон:\n<a href="ССЫ'
                  'ЛКА">КЛИКАБЕЛЬНЫЙ ТЕКСТ</a>. Для удобства:\n\n<a href="'
                  '"></a>',
    )
    slug = SlugField(
        max_length=128, unique=True, verbose_name='Ссылка',
        help_text='Можно оставить пустым', blank=True,
    )
    start = DateTimeField(verbose_name='Дата и время')
    place = ForeignKey(
        to='Bar', related_name='ivents', on_delete=CASCADE,
        verbose_name='Место'
    )
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )
    image = ImageField(
        upload_to='events_images',
        verbose_name='Фото',
        blank=True
    )

    class Meta:
        verbose_name = 'ивенты'
        verbose_name_plural = 'Ивент'

    def get_status(self):
        now = timezone.now()
        if self.start > now:
            return 'Ещё не началось'
        elif now <= self.start < now + timedelta(hours=3):
            return 'Уже началось'
        return 'Закончилось'

    def get_absolute_url(self):
        return reverse('app_setofshots:event', kwargs={'event_slug': self.slug})

    def __str__(self):
        return f'{self.title}, {self.start}.'


class Dish(Model):
    title = CharField(max_length=32, verbose_name='Название')
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка',
        help_text='Заполняется автоматически(если такая ссылка уже существует, '
                  'стоит добавить постфикс "_<рюмочная>", например: "..._zin"',
        blank=True,
    )
    category = ForeignKey(
        Category, on_delete=CASCADE,
        null=False, related_name='dishes', verbose_name='Категория'
    )
    description = CharField(max_length=1024, verbose_name='Описание')
    tags = ManyToManyField(Tag, through='TagDish', verbose_name='Теги')
    price = IntegerField(verbose_name='Цена')
    promille = IntegerField(
        verbose_name='Крепость', help_text='Если не алкоголь- оставить пустым',
        blank=True, null=True
    )
    bar = ForeignKey(
        'Bar', on_delete=CASCADE, null=False, related_name='dishes',
        default=None
    )
    image = ImageField(
        upload_to='dishes_images',
        verbose_name='Фото',
        blank=True
    )
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

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
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка',
        help_text='Можно оставить пустым', blank=True,
    )
    description = CharField(max_length=1024, verbose_name='Описание')
    address = CharField(max_length=128, verbose_name='Адрес')
    opening_year = IntegerField(verbose_name='Год открытия')
    image = ImageField(
        upload_to='bars_images',
        verbose_name='Фото',
        blank=True
    )
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

    class Meta:
        verbose_name = 'бар'
        verbose_name_plural = 'Бары'

    def __str__(self):
        return self.title


class TagDish(Model):
    tag = ForeignKey(Tag, on_delete=CASCADE)
    dish = ForeignKey(Dish, on_delete=CASCADE)

    def __str__(self):
        return f'Теги для{self.dish}: {self.tag}'


class Post(Model):
    title = CharField(max_length=128, verbose_name='Заголовок')
    slug = SlugField(
        max_length=64, unique=True, verbose_name='Ссылка',
        help_text='Можно оставить пустым', blank=True,
    )
    text = TextField(max_length=2048, verbose_name='Текст')
    bar = ForeignKey(
        'Bar', on_delete=CASCADE,
        null=True, blank=True,
        related_name='posts', verbose_name='Место',
        help_text='Можно оставить пустым',
    )
    is_published = BooleanField(
        verbose_name='Опубл.', blank=True, default=False
    )
    pub_datetime = DateTimeField(
        verbose_name='Дата публикации',
        auto_created=True, null=True
    )
    image = ImageField(
        upload_to='posts_images',
        verbose_name='Фото',
        blank=True
    )

    class Meta:
        ordering = ('-pub_datetime',)
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('app_setofshots:feed', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title[:64]
