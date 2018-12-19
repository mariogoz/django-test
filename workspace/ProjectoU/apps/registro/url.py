
from django.urls import path
from apps.registro.views import index
from apps.registro.success import success
urlpatterns = [
    path('', index),
    path('success', success),
]
