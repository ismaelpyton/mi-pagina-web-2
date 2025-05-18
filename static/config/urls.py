from django.contrib import admin
from django.urls import path, include
from inicio import urls as inicio_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(inicio_urls)),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
