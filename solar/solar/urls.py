from django.contrib import admin
from django.urls import path, include
from .views import testando
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/', testando),
    path('', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
