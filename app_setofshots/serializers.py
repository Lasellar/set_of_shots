from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField, CharField,
    ListField, DictField
)
import datetime as dt
from pytz import utc

from .models import (
    Bar, Event, Dish, Category, Tag
)


class CategorySerializer(ModelSerializer):
    title = CharField()

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    title = CharField()

    class Meta:
        model = Tag
        fields = '__all__'


class _EventSerializer(ModelSerializer):
    status = SerializerMethodField()
    start = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_start(self, obj):
        return obj.start.strftime('%Y.%m.%d %H:%M')

    def get_status(self, obj):
        now = dt.datetime.now(utc)
        start = obj.start.replace(tzinfo=utc)
        if now < start:
            return 'Ещё не началось'
        elif start <= now < start + dt.timedelta(hours=3):
            return 'Уже началось'
        return 'Закончилось'


class BarSerializer(ModelSerializer):
    title = CharField()

    class Meta:
        model = Bar
        fields = (
            'title',
            'slug',
            'description',
            'address',
            'opening_year',
        )


class EventSerializer(ModelSerializer):
    status = SerializerMethodField()
    start = SerializerMethodField()
    place = BarSerializer(required=True)

    class Meta:
        model = Event
        fields = '__all__'

    def get_start(self, obj):
        return obj.start.strftime('%Y.%m.%d %H:%M')

    def get_status(self, obj):
        now = dt.datetime.now(utc)
        start = obj.start.replace(tzinfo=utc)
        if now < start:
            return 'Ещё не началось'
        elif start <= now < start + dt.timedelta(hours=3):
            return 'Уже началось'
        return 'Закончилось'


class DishSerializer(ModelSerializer):
    category = CategorySerializer(required=True)
    bar = BarSerializer(required=True)

    class Meta:
        model = Dish
        fields = '__all__'
