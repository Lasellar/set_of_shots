from django.urls import path

from .views import events, bars, feeds, feed, menu, event, bar

app_name = 'app_setofshots'

urlpatterns = [
    path('', feeds, name='feeds'),
    path('bars/', bars, name='bars'),
    path('events/', events, name='events'),

    path('events/<slug:event_slug>/', event, name='event'),
    path('feeds/<slug:post_slug>/', feed, name='feed'),
    path('bars/<slug:bar_slug>/', bar, name='bar'),
    path('menu/<slug:bar_slug>/', menu, name='menu'),

]
