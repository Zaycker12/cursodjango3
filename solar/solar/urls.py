from django.contrib import admin
from django.urls import path, include
from .views import testando


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/', testando),
    path('solar', include('website.urls')),
]
