from django.test import TestCase
from shop.models import Product, Category
from orders.models import Order, OrderItem

class OrderTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            nombre="Electrónica",
            slug="electronica"
        )

        self.product = Product.objects.create(
            nombre="Producto de prueba",
            precio=10.0,
            cantidad=100,
            categoria=self.category
        )

        self.order = Order.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            address="123 Main St",
            postal_code="12345",
            city="Test City"
        )

    def test_create_order_item_succesful(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=self.product.precio
        )
        
        self.assertEqual(order_item.product, self.product)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.price, self.product.precio)

    def test_create_order_succesful(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
            price=self.product.precio
        )

        self.assertEqual(self.order.items.count(), 1) 
        self.assertEqual(order_item.quantity, 3)
        self.assertEqual(order_item.price, self.product.precio)
