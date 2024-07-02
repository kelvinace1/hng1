from django.urls import path
from . import views

urlpatterns = [
    path('api/hello', views.get_weather , name='get_weather') 
]
