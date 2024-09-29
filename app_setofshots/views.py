from itertools import chain

from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from setofshots import settings

from .models import (
    Bar, Event, Dish, Post
)


def paginator(object_list, page):
    """Вспомогательная функция, возвращающая объект страницы."""
    _paginator = Paginator(
        object_list,
        settings.REST_FRAMEWORK['PAGE_SIZE']
    )
    return _paginator.get_page(page)


def feeds(request):
    """View-функция, которая рендерит страницу с новостями."""
    template = 'app_setofshots/feeds.html'
    _posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    _events = Event.objects.filter(
        is_published=True).order_by('-start')
    objects = list(chain(_events, _posts))
    page_object = paginator(objects, request.GET.get('page'))
    context = {'page_obj': page_object}
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
    bar_dishes = Dish.objects.filter(bar=_bar, is_published=True
                                     ).prefetch_related('tags')
    context = {'bar': _bar, 'bar_dishes': bar_dishes}
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
    template = 'app_setofshots/detail_event.html'
    _event = get_object_or_404(Event, slug=event_slug, is_published=True)
    context = {'event': _event}
    return render(request, template, context)


def menu(request):
    template = 'app_setofshots/menu.html'
    context = {}
    return render(request, template, context)
