from django.contrib import admin

from .models import Bar, Tag, Category, Dish, Event

admin.site.empty_value_display = '---'


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_list')
    # filter_horizontal = ('dishes',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)
