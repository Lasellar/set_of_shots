from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.log import log_response

from .models import (
    Bar, Tag, Category, Dish, Event, Post, TagDish,
    BarUnderground, Underground, AttachmentImage
)
from .forms import EventForm

admin.site.empty_value_display = '---'


class DishInline(admin.TabularInline):
    model = Dish
    extra = 0
    fields = ('title', 'price')
    ordering = ('title',)


class UndergroundInline(admin.StackedInline):
    model = BarUnderground
    extra = 1


class AttachmentImageInline(admin.StackedInline):
    model = AttachmentImage
    extra = 1
    fields = ('image', 'is_published')


@admin.register(AttachmentImage)
class AttachmentImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_published')
    list_editable = ('is_published',)


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published',)
    inlines = (UndergroundInline, AttachmentImageInline, DishInline)
    prepopulated_fields = {'slug': ('title',)}
    actions = ('set_published', 'unset_published')

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, f'Изменено {count} записей', messages.WARNING
        )

    @admin.display(description='Снять с публикации')
    def unset_published(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request, f'{count} записей снято с публикации', messages.WARNING
        )


class TagDishInline(admin.TabularInline):
    model = TagDish
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'bar__title', 'is_published', 'short_description', 'price')
    list_editable = ('price', 'is_published',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (TagDishInline,)
    actions = ('set_published', 'unset_published')
    list_filter = ('is_published', 'bar__title',)

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, f'Изменено {count} записей', messages.WARNING
        )

    @admin.display(description='Снять с публикации')
    def unset_published(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request, f'{count} записей снято с публикации', messages.WARNING
        )

    @admin.display(description='Описание', ordering='description')
    def short_description(self, obj: Post):
        return obj.description[:25] + '...' if len(obj.description) > 28 \
            else obj.description


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published',)


@admin.register(Underground)
class UndergroundAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'title', 'is_published')
    list_editable = ('is_published',)

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:10px; height: auto;">',
                obj.image.url
            )
        return ' '


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'is_published')
    list_editable = ('is_published',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    actions = ('set_published', 'unset_published')

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, f'Изменено {count} записей', messages.WARNING
        )

    @admin.display(description='Снять с публикации')
    def unset_published(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request, f'{count} записей снято с публикации', messages.WARNING
        )

    @admin.display(description='Название', ordering='title')
    def short_title(self, obj: Post):
        return obj.title[:15] + '...' if len(obj.title) > 18 else obj.title


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('short_title', 'is_published', 'short_description')
    list_editable = ('is_published',)
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_filter = ('is_published', 'place__title',)
    actions = ('set_published', 'unset_published')
    fields = ('title', 'description',
              'slug', 'start', 'place', 'is_published', 'image')

    @admin.display(description='Название', ordering='title')
    def short_title(self, obj: Post):
        return obj.title[:15] + '...' if len(obj.title) > 18 else obj.title

    @admin.display(description='Текст', ordering='text')
    def short_description(self, obj: Post):
        return obj.description[:25] + '...' if len(obj.description) > 28 \
            else obj.description

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, f'Изменено {count} записей', messages.WARNING
        )

    @admin.display(description='Снять с публикации')
    def unset_published(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request, f'{count} записей снято с публикации', messages.WARNING
        )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('is_published', 'short_title', 'short_text',)
    list_editable = ('is_published',)
    list_display_links = ('short_title',)
    list_per_page = 10
    ordering = ('-pub_datetime', '-id',)
    actions = ('set_published', 'unset_published')
    search_fields = ('title', 'text', 'pub_datetime',)
    search_help_text = 'Поиск по названию/тексту/дате'
    list_filter = ('is_published', 'bar__title',)
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        'title', 'text', 'bar', 'slug', 'pub_datetime', 'is_published', 'image'
    )

    @admin.display(description='Название', ordering='title')
    def short_title(self, obj: Post):
        return obj.title[:15] + '...' if len(obj.title) > 18 else obj.title

    @admin.display(description='Текст', ordering='text')
    def short_text(self, obj: Post):
        return obj.text[:25] + '...' if len(obj.text) > 28 else obj.text

    @admin.display(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, f'Изменено {count} записей', messages.WARNING
        )

    @admin.display(description='Снять с публикации')
    def unset_published(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(
            request, f'{count} записей снято с публикации', messages.WARNING
        )
