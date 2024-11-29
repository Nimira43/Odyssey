from django.urls import path
from odyssey.views import home

urlpatterns = [
  path('', home),
]

