from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('detalles_pedido/<str:codigo>/', views.detalles_pedido, name='detalles_pedido'),
    path('buscar_pedido/', views.buscar_pedido, name='buscar_pedido'),
    path('create/', views.order_create, name='order_create'),
]