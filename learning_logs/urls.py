"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

spp_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
]