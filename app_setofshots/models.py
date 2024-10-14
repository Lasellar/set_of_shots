from datetime import timedelta

from django.db.models import (
    Model,
    CharField, IntegerField,
    ForeignKey, ManyToManyField,
    ImageField, SlugField, BooleanField,
    CASCADE, TextField, DateTimeField,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


class Tag(Model):
    title = CharField(max_length=128, verbose_name='Название')
    is_published = BooleanField(
        verbose_name='Опубл.', blank=True, default=False
    )
    background_color = CharField(
        max_length=7,
        verbose_name='Цвет фона',
        help_text='цвет фона должен быть в формате #000000(может быть пустым)',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'

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
                  'на слово)<br>следует использовать шаблон:<br>&lt;a hre'
                  'f="ССЫЛКА"&gt;КЛИКАБЕЛЬНЫЙ ТЕКСТ&lt;/a&gt;. Шаблон для'
                  ' удобства:<br><br>&lt;a href=""&gt;&lt;/a&gt;',
    )
    slug = SlugField(
        max_length=128, unique=True, verbose_name='Ссылка',
        help_text='Можно оставить пустым', blank=True,
    )
    start = DateTimeField(verbose_name='Дата и время')
    duration = IntegerField(
        verbose_name='Длительность в часах',
        null=True, blank=True, help_text='По умолчанию 3 часа'
    )
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
        verbose_name = 'ивент'
        verbose_name_plural = 'Ивенты'

    def get_absolute_url(self):
        """Добавление ссылки 'смотреть на сайте' в админку"""
        return reverse('app_setofshots:event', kwargs={'event_slug': self.slug})

    def __str__(self):
        return f'{self.title}, {self.start}.'


class Dish(Model):
    title = CharField(max_length=32, verbose_name='Название')
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка',
        help_text='Заполняется автоматически(если такая ссылка уже существует, '
                  'стоит добавить постфикс "_<рюмочная>", например: "..._zin")',
        blank=True,
    )
    category = ForeignKey(
        Category, on_delete=CASCADE,
        null=False, related_name='dishes', verbose_name='Категория'
    )
    description = TextField(max_length=1024, verbose_name='Описание')
    tags = ManyToManyField(Tag, through='TagDish', verbose_name='Теги')
    price = IntegerField(verbose_name='Цена')
    promille = IntegerField(
        verbose_name='Крепость', help_text='Если не алкоголь- оставить пустым',
        blank=True, null=True
    )
    bar = ForeignKey(
        'Bar', on_delete=CASCADE, null=False, related_name='dishes',
        default=None, verbose_name='Рюмочная'
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


class Underground(Model):
    title = CharField(max_length=40, verbose_name='Станция')
    image = ImageField(
        upload_to='ug_images', verbose_name='Значок', blank=True)
    is_published = BooleanField(
        verbose_name='Опубл.', blank=True, default=False
    )

    class Meta:
        verbose_name = 'метро'
        verbose_name_plural = 'Метро'

    def __str__(self):
        return self.title


class Bar(Model):
    title = CharField(max_length=32, verbose_name='Бар')
    slug = SlugField(
        max_length=32, unique=True, verbose_name='Ссылка',
        help_text='Можно оставить пустым', blank=True,
    )
    description = TextField(max_length=1024, verbose_name='Описание')
    address = CharField(max_length=128, verbose_name='Адрес')

    work_time_monday = CharField(max_length=11, verbose_name='Часы работы(пн)', null=True)
    work_time_tuesday = CharField(max_length=11, verbose_name='Часы работы(вт)', null=True)
    work_time_wednesday = CharField(max_length=11, verbose_name='Часы работы(ср)', null=True)
    work_time_thursday = CharField(max_length=11, verbose_name='Часы работы(чт)', null=True)
    work_time_friday = CharField(max_length=11, verbose_name='Часы работы(пт)', null=True)
    work_time_saturday = CharField(max_length=11, verbose_name='Часы работы(сб)', null=True)
    work_time_sunday = CharField(max_length=11, verbose_name='Часы работы(вс)', null=True)

    telegram_link = CharField(
        max_length=100, verbose_name='Ссылка на тг-канал',
        help_text='можно оставить пустым', null=True, blank=True
    )
    instagram_link = CharField(
        max_length=100, verbose_name='Ссылка на инстаграм',
        help_text='можно оставить пустым', null=True, blank=True
    )
    yandex_maps_link = CharField(
        max_length=2048, verbose_name='Ссылка на карты',
        help_text='Лучше оставить пустым', null=True, blank=True
    )
    image = ImageField(
        upload_to='bars_images',
        verbose_name='Главное Фото',
        blank=True
    )
    underground = ManyToManyField(
        Underground, through='BarUnderground', verbose_name='Метро')
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

    class Meta:
        verbose_name = 'бар'
        verbose_name_plural = 'Бары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app_setofshots:bar', kwargs={'bar_slug': self.slug})


class AttachmentImage(Model):
    image = ImageField(
        upload_to='attachment_images',
        verbose_name='Фото для карусели',
        blank=True,
    )
    bar = ForeignKey(
        to=Bar, related_name='attachment_images', on_delete=CASCADE,
        verbose_name='Рюмочная'
    )
    is_published = BooleanField(
        verbose_name='Опубликовано', blank=True, default=False
    )

    class Meta:
        verbose_name = 'фото для карусели'
        verbose_name_plural = 'Фото для карусели'

    def __str__(self):
        return self.image.name


class BarUnderground(Model):
    bar = ForeignKey(Bar, on_delete=CASCADE)
    underground = ForeignKey(Underground, on_delete=CASCADE)


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
    text = TextField(
        max_length=2048, verbose_name='Текст',
        help_text=f'Для вставки красивых ссылок(чтобы можно было кликать '
                  'на слово)<br>следует использовать шаблон:<br>&lt;a hre'
                  'f="ССЫЛКА"&gt;КЛИКАБЕЛЬНЫЙ ТЕКСТ&lt;/a&gt;. Шаблон для'
                  ' удобства:<br><br>&lt;a href=""&gt;&lt;/a&gt;',
    )
    bar = ForeignKey(
        Bar, on_delete=CASCADE,
        null=True, blank=True,
        related_name='posts', verbose_name='Место',
        help_text='Можно оставить пустым',
    )
    is_published = BooleanField(
        verbose_name='Опубл.', blank=True, default=False
    )
    pub_datetime = DateTimeField(
        verbose_name='Дата публикации',
        auto_created=True, null=True,
        help_text='Если поставить дату и время в будущем- публикация'
                  'Будет отложена и опубликуется автоматически в ука'
                  'занное время'
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
