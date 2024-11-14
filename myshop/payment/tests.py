from django.urls import reverse
from django.test import TestCase
from orders.models import Order, OrderItem
from shop.models import Product, Category
from django.contrib.auth.models import User

class PaymentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.category = Category.objects.create(nombre="Test Category", slug="test-category")
        self.product = Product.objects.create(
            nombre="Test Product",
            slug="test-product",
            categoria=self.category,
            precio=20.00,
            cantidad=10
        )
        
        session = self.client.session
        session['cart'] = {
            str(self.product.id): {'quantity': 1, 'price': str(self.product.precio)}
        }
        session.save()

        response = self.client.post(reverse('orders:order_create'), {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'address': '123 Street',
            'postal_code': '12345',
            'city': 'Test City'
        })


    def test_payment_process_get(self):
        response = self.client.get(reverse('payment:process'))
        self.assertEqual(response.status_code, 200)

    def test_payment_done(self):
        response = self.client.get(reverse('payment:done'))
        self.assertEqual(response.status_code, 200)

    def test_payment_canceled(self):
        response = self.client.get(reverse('payment:canceled'))
        self.assertEqual(response.status_code, 200)
