from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from http import HTTPStatus

from .models import (
    Bar, Event, Dish, Post
)
from .serializers import (
    BarSerializer, EventSerializerWithPlace,
    DishSerializer, EventSerializerWithoutPlace, PostSerializer
)


@api_view(['GET'])
def get_bars(request):
    bars = Bar.objects.all()
    serializer = BarSerializer(bars, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializerWithPlace(events, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_dishes(request):
    dishes = Dish.objects.all()
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_bar(request, bar_slug):
    bar = get_object_or_404(Bar, slug=bar_slug)
    bar_serializer = BarSerializer(bar)
    events = Event.objects.filter(place=bar)
    event_serializer = EventSerializerWithoutPlace(events, many=True)
    response_data = {
        'bar': bar_serializer.data,
        'events': event_serializer.data
    }
    return Response(data=response_data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_bar_events(request, bar_slug=None):
    events = Event.objects.all()
    if bar_slug is not None:
        bar = get_object_or_404(Bar, slug=bar_slug)
        events = events.filter(place=bar)
    serializer = EventSerializerWithPlace(events, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.filter(is_published=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=HTTPStatus.OK)
