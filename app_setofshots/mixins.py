from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer, CharField
)

from app_setofshots.models import Event, Bar, Category


class CategorySerializerMixin(ModelSerializer):
    title = CharField()

    class Meta:
        model = Category
        fields = '__all__'


class BarSerializerMixin(ModelSerializer):
    title = CharField()

    class Meta:
        model = Bar
        fields = '__all__'
