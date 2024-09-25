from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from app_setofshots.views import (
    get_bars, get_events, get_dishes,
    get_bar_events, get_bar, get_posts, get_post
)

router = routers.DefaultRouter()

urlpatterns = [

    path('posts/', get_posts, name='posts'),
    path('bars/', get_bars, name='get_bars'),
    path('events/', get_events, name='get_events'),
    path('dishes/', get_dishes, name='get_dishes'),

    path('posts/<slug:post_slug>/', get_post, name='post'),
    path('bars/<slug:bar_slug>/events/', get_bar_events),
    path('bars/<slug:bar_slug>/', get_bar),
    path('admin/', admin.site.urls),

]
admin.site.site_header = 'Админ-панель'
admin.site.index_title = ''
admin.site.site_title = 'Админка Сет рюмочных'
admin.site.empty_value_display = '   '

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)