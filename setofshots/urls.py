from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('', include('app_setofshots.urls', namespace='app_setofshots')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

admin.site.site_header = 'Админ-панель'
admin.site.index_title = ''
admin.site.site_title = 'Админка Сет рюмочных'
admin.site.empty_value_display = '   '

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)