from django.contrib import admin

from .models import Bar, Tag, Category, Dish, Event

admin.site.empty_value_display = '---'


class DishInline(admin.TabularInline):
    model = Dish
    extra = 0
    fields = ('title', 'price')
    readonly_fields = ('title',)
    ordering = ('title',)


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (DishInline,)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price')
    list_editable = ('price',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)
