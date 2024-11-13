# archivo: urls.py

from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('cancelled/', views.payment_cancelled, name='cancelled'),
    path('', include('shop.urls', namespace='shop')),  # Esto incluye las URLs de 'shop'
]