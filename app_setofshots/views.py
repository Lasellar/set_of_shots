from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from http import HTTPStatus
import json

from .models import (
    Bar, Event, Dish
)
from .serializers import (
    BarSerializer, EventSerializer,
    DishSerializer
)


@api_view(['GET'])
def get_bars(request):
    bars = Bar.objects.all()
    serializer = BarSerializer(bars, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
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
    event_serializer = EventSerializer(events, many=True)
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
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)
