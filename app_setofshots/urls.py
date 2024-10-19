from django.urls import path

from .views import events, bars, feeds, feed, menu, event, bar, logs

app_name = 'app_setofshots'

urlpatterns = [
    path('', feeds, name='feeds'),
    path('bars/', bars, name='bars'),
    path('events/', events, name='events'),
    path('a1b2C3d4E5f6G7h8/logs/<int:year>/<int:month>/<int:day>/', logs, name='logs'),

    path('events/<slug:event_slug>/', event, name='event'),
    path('feeds/<slug:post_slug>/', feed, name='feed'),
    path('bars/<slug:bar_slug>/', bar, name='bar'),
    path('menu/<slug:bar_slug>/', menu, name='menu'),
]
