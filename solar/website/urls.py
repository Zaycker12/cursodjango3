from django.urls import path, include
from .views import hello_solar


urlpatterns = [
    path('', hello_solar),
    
]
