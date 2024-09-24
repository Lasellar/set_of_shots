from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from app_setofshots.views import (
    get_bars, get_events, get_dishes,
    get_bar_events, get_bar
)

router = routers.DefaultRouter()

urlpatterns = [

    path('bars/', get_bars, name='get_bars'),
    path('events/', get_events, name='get_events'),
    path('dishes/', get_dishes, name='get_dishes'),

    path('bars/<slug:bar_slug>/events/', get_bar_events),
    path('bars/<slug:bar_slug>/', get_bar),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)