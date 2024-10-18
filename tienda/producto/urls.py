from django.urls import path
from .views import insertar_producto

urlpatterns = [
    path('insertar/', insertar_producto, name='insertar-pro'),
]

