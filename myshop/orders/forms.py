from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellidos', 'email', 'dirección',
                  'código_postal', 'ciudad']