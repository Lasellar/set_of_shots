from django.db.models import Model
from django.utils.text import slugify
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer, CharField
)

from app_setofshots.models import Event, Bar, Category, Post

import datetime as dt
from pytz import utc


class CategorySerializerMixin(ModelSerializer):
    title = CharField()

    class Meta:
        model = Category
        fields = '__all__'


class EventSerializerMixin(ModelSerializer):
    status = SerializerMethodField()
    start = SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'is_piblished'
            'description',
            'slug',
            'status',
            'start',
        )

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


class BarSerializerMixin(ModelSerializer):
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
