
from django.urls import path
from apps.registro.views import index
urlpatterns = [
    path('', index),
]
