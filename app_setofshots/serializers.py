import datetime

from rest_framework.serializers import ModelSerializer, SerializerMethodField

import setofshots.settings
from .mixins import BarSerializerMixin, CategorySerializerMixin
from .models import (
    Bar, Event, Dish, Category, Tag, Post, Underground, AttachmentImage
)


class UndergroundSerializer(ModelSerializer):
    class Meta:
        model = Underground
        fields = ('title',)


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('is_published',)


class AttachmentImageSerializer(ModelSerializer):
    class Meta:
        model = AttachmentImage
        fields = ('image',)


class CategorySerializer(CategorySerializerMixin):
    pass


class CategorySerializerForDishes(CategorySerializerMixin):
    class Meta:
        model = Category
        fields = ('title',)


class BarSerializer(BarSerializerMixin):
    underground = UndergroundSerializer(required=True, many=True)
    attachment_images = AttachmentImageSerializer(many=True, required=False)

    class Meta:
        model = Bar
        fields = '__all__'


class BarSerializerForDishes(BarSerializerMixin):
    class Meta:
        model = Bar
        fields = ('title', 'slug')


class EventSerializer(ModelSerializer):
    place = BarSerializerForDishes(required=True)
    formatted_start = SerializerMethodField()
    status = SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_formatted_start(self, obj):
        return obj.start.strftime('%d.%m.%Y %H:%M')

    def get_status(self, obj):
        now = datetime.datetime.now(
            datetime.timezone.utc) + datetime.timedelta(hours=3)
        print(now)
        start = obj.start
        if start > now:
            return 'Ещё не началось'
        if obj.duration:
            if start <= now < start + datetime.timedelta(hours=obj.duration):
                return 'Уже идёт'
        else:
            if start <= now < start + datetime.timedelta(hours=3):
                return 'Уже идёт'
        return 'Закончилось'


class DishSerializer(ModelSerializer):
    category = CategorySerializerForDishes(required=True)
    bar = BarSerializerForDishes(required=True)
    tags = TagSerializer(required=True, many=True)

    class Meta:
        model = Dish
        fields = '__all__'


class PostSerializer(ModelSerializer):
    bar = BarSerializer()

    class Meta:
        model = Post
        fields = '__all__'
