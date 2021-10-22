from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('bienvenidos', views.bienvenidos,name='bienvenidos'),
]
