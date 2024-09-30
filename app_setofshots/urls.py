from django.urls import path

from .views import (
    feeds, feed, bar, bars, events, bar_events, event, menu,

)

app_name = 'app_setofshots'

urlpatterns = [
    path('', feeds, name='feeds'),
    path('bars/', bars, name='bars'),
    path('events/', events, name='events'),
    path('menu/<slug:bar_slug>/', menu, name='menu'),
    path('menu/', menu, name='menu'),
    # path('dishes/', get_dishes, name='get_dishes'),

    # path('menu/<slug:bar_slug>/', menu, name='menu_bar'),
    path('events/<slug:event_slug>/', event, name='event'),
    path('feeds/<slug:post_slug>/', feed, name='feed'),
    path('bars/<slug:bar_slug>/events/', bar_events),
    path('bars/<slug:bar_slug>/', bar, name='bar'),
]
