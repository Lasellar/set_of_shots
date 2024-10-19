import datetime
from functools import wraps
from pathlib import Path

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from http import HTTPStatus

from .models import (
    Bar, Event, Dish, Post
)
from .serializers import (
    BarSerializer,
    DishSerializer, PostSerializer, EventSerializer
)
from .logger.logger import log_decorator


@api_view(['GET'])
@log_decorator
def bars(request):
    _bars = Bar.objects.all()
    serializer = BarSerializer(_bars, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def bar(request, bar_slug):
    _bar = get_object_or_404(Bar, slug=bar_slug)
    serializer = BarSerializer(_bar)
    return Response(data=serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def events(request):
    _events = Event.objects.all()
    serializer = EventSerializer(_events, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def event(request, event_slug):
    _event = get_object_or_404(Event, slug=event_slug)
    serializer = EventSerializer(_event)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def menu(request, bar_slug):
    dishes = Dish.objects.filter(bar__slug=bar_slug)
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def feeds(request):
    posts = Post.objects.filter(is_published=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
@log_decorator
def feed(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=HTTPStatus.OK)


@log_decorator
def logs(request, year, month, day):
    _DIR_ = Path(__file__).resolve().parent
    path_to_file = _DIR_ / 'logger' / 'logs' / str(year) / str(month) / f'{day}.html'
    with open(path_to_file, 'r') as file:
        html_content = file.read()
    return HttpResponse(html_content)

