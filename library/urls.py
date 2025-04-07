from django.contrib import admin
from django.urls import path

# Views import
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
