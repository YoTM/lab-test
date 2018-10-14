from django.urls import path

from .views import pays_monitor

urlpatterns = [
    path('', pays_monitor),
]