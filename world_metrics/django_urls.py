from django.urls import path
from .django_views import counters
urlpatterns = [path("all", counters)]
