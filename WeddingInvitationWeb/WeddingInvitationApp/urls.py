from django.urls import path
from . import views

urlpatterns = [
    path('rsvp/', views.rsvp, name='rsvp'),
    path('success/', views.success, name='success'),
    path('stats/', views.stats, name='stats'),
]