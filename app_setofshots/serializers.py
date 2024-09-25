from rest_framework.serializers import (
    ModelSerializer, CharField,
)

from .mixins import EventSerializerMixin, BarSerializerMixin, CategorySerializerMixin
from .models import (
    Bar, Event, Dish, Category, Tag, Post
)


class CategorySerializer(CategorySerializerMixin):
    pass


class CategorySerializerForDishes(CategorySerializerMixin):
    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(ModelSerializer):
    title = CharField()

    class Meta:
        model = Tag
        fields = '__all__'


class BarSerializer(BarSerializerMixin):
    pass


class BarSerializerForDishes(BarSerializerMixin):
    class Meta:
        model = Bar
        fields = ('title', 'slug')


class EventSerializerWithPlace(EventSerializerMixin):
    place = BarSerializer(required=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializerWithoutPlace(EventSerializerMixin):
    class Meta:
        model = Event
        exclude = ('place',)


class DishSerializer(ModelSerializer):
    category = CategorySerializerForDishes(required=True)
    bar = BarSerializerForDishes(required=True)

    class Meta:
        model = Dish
        fields = (
            'id',
            'title',
            'unique_dish_id',
            'slug',
            'price',
            'tags',
            'description',
            'category',
            'bar'
        )


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'bar',
            'pub_date',
            'is_published'
        )
