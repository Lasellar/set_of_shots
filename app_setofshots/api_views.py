import datetime
from itertools import chain

from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from setofshots import settings

from .models import (
    Bar, Event, Dish, Post, Category, AttachmentImage
)


def paginator(object_list, page):
    """Вспомогательная функция, возвращающая объект страницы."""
    _paginator = Paginator(
        object_list,
        settings.REST_FRAMEWORK['PAGE_SIZE']
    )
    return _paginator.get_page(page)


def feeds(request):
    """
    View-функция, которая рендерит страницу с новостями.
    Получает посты и ивенты, соединяет их в один список
    и создает объект страницы.
    """
    template = 'app_setofshots/feeds.html'
    _posts = Post.objects.filter(
        is_published=True,
        pub_datetime__lte=timezone.now()
    ).order_by('-pub_datetime')
    _events = Event.objects.filter(
        is_published=True).order_by('-start')
    objects = list(chain(_events, _posts))
    page_object = paginator(objects, request.GET.get('page'))
    context = {
        'page_obj': page_object
    }
    return render(request, template, context)


def feed(request, post_slug):
    """View-функция, которая рендерит отдельную страницу новости."""
    template = 'app_setofshots/detail_feed.html'
    post = get_object_or_404(Post, slug=post_slug, is_published=True)
    context = {'post': post}
    return render(request, template, context)


def bars(request):
    """View-функция, которая рендерит страницу с барами."""
    template = 'app_setofshots/bars.html'
    _bars = Bar.objects.filter(is_published=True)
    page_object = paginator(_bars, request.GET.get('page'))
    context = {'page_obj': page_object}
    return render(request, template, context)


def bar(request, bar_slug):
    """View-функция, которая рендерит отдельную страницу новости."""
    template = 'app_setofshots/detail_bar.html'
    _bar = get_object_or_404(Bar, slug=bar_slug, is_published=True)
    carousel = AttachmentImage.objects.filter(bar=_bar, is_published=True)
    print(carousel)
    context = {'bar': _bar, 'carousel': carousel}
    return render(request, template, context)


def bar_events(request, bar_slug):
    """View-функция, которая рендерит страницу с ивентами бара."""
    template = 'app_setofshots/bar_events.html'
    _bar = get_object_or_404(Bar, slug=bar_slug, is_published=True)
    _events = Event.objects.filter(place=_bar, is_published=True
                                   ).order_by('-start')
    page_object = paginator(_events, request.GET.get('page'))
    context = {'page_obj': page_object}
    return render(request, template, context)


def events(request):
    """View-функция, которая рендерит страницу со всеми ивентами."""
    template = 'app_setofshots/events.html'
    _events = Event.objects.filter(
        is_published=True).order_by('-start')
    page_object = paginator(_events, request.GET.get('page'))
    context = {'page_obj': page_object}
    return render(request, template, context)


def event(request, event_slug):
    """View-функция, которая редерит отдельную страницу ивента."""
    template = 'app_setofshots/detail_event.html'
    _event = get_object_or_404(Event, slug=event_slug, is_published=True)
    context = {
        'event': _event,
    }
    return render(request, template, context)


def menu(request, bar_slug=None):
    """
    View-функция, которая рендерит страницу с меню.
    При первом открытии страницы(на эндпоинте /menu/
    и без параметров запроса) не выводит никакие позиции.
    Можно выбрать конкретный интересующий бар, ссылки
    на которые находятся в кнопках с названиями.
    Названия как и категории берутся из базы данных и
    создаются в админке. Кнопки категорий при нажатии
    не дополняют эндпоинт, а добавляют параметры в запрос.
    """
    template = 'app_setofshots/menu.html'
    _bars = Bar.objects.filter(is_published=True)
    _categories = Category.objects.filter(is_published=True)

    # Фильтруем блюда по выбранному бару и категориям
    _dishes = Dish.objects.filter(
        is_published=True
    )

    if bar_slug:
        _dishes = _dishes.filter(bar__slug=bar_slug)
    else:
        _dishes = []

    __categories = request.GET.getlist('category')
    for _category in __categories:
        _dishes = _dishes.filter(category__slug=_category)

    page_object = paginator(_dishes, request.GET.get('page'))

    context = {
        'bars': _bars,
        'categories': _categories,
        'page_obj': page_object,
        'categories_': __categories
    }
    return render(request, template, context)


def logs(request):
    template = 'logs.html'
    content = ...
    context = {'content': content}
