from django.contrib import admin
from django.urls import path
from rest_framework import routers

from app_setofshots.views import get_list_of_bars

router = routers.DefaultRouter()

urlpatterns = [
    path('bars/', get_list_of_bars, name='get_list_of_bars'),
    path('admin/', admin.site.urls),
]
