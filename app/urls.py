from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:present_class>', views.index),
    path('', views.index)
]