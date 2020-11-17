from django.urls import path, include
from .views import hello_solar
from .views import post_detail


urlpatterns = [
    path('', hello_solar, name='home_solar'),
    path ('post/<int:id>/', post_detail, name= 'post_detail')

]
