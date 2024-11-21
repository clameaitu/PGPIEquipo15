from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from shop.models import Product, Category
from orders.models import Order
from decimal import Decimal


class PaymentTests(TestCase):
    def setUp(self):
        # Crear un usuario para el test
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        # Crear una categoría y producto
        self.category = Category.objects.create(nombre="Velas", slug="velas")
        self.product = Product.objects.create(
            categoria=self.category,
            nombre="velas_naranja",
            slug="velas-naranja",
            precio=Decimal("699.99"),
            cantidad=10
        )
        
        # Simular un carrito en la sesión
        session = self.client.session
        session['cart'] = {
            str(self.product.id): {'quantity': 1, 'price': str(self.product.precio)}
        }
        session.save()
        
        # Crear un pedido a través de la vista
        self.client.post(reverse('orders:order_create'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'address': '123 Main Street',
            'postal_code': '12345',
            'city': 'Test City'
        })
        self.order = Order.objects.last()

def test_payment_process_get(self):
    response = self.client.get(reverse('payment:process'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Procesar pago")

def test_payment_done(self):
    """Probar que la vista de pago completado se cargue correctamente."""
    response = self.client.get(reverse('payment:done'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Gracias por su compra")

def test_payment_canceled(self):
    """Probar que la vista de cancelación de pago se cargue correctamente."""
    response = self.client.get(reverse('payment:canceled'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Your payment has not been processed")

