from django.test import TestCase
from shop.models import Product, Category
from orders.models import Order, OrderItem

class OrderTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            nombre="Colonias",
            slug="colonias"
        )

        self.product = Product.objects.create(
            nombre="Producto de prueba",
            precio=10.0,
            cantidad=100,
            categoria=self.category
        )

        self.order = Order.objects.create(
            nombre="John",
            apellidos="Doe",
            email="john@example.com",
            dirección="123 Main St",
            código_postal="12345",
            ciudad="Test City",
            entrega_en_oficina_de_correos="False"
        )

    def test_create_order_item_succesful(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            producto=self.product,
            cantidad=2,
            precio=self.product.precio
        )
        
        self.assertEqual(order_item.producto, self.product)
        self.assertEqual(order_item.cantidad, 2)
        self.assertEqual(order_item.order, self.order)
        self.assertEqual(order_item.precio, self.product.precio)

    def test_create_order_succesful(self):
        order_item = OrderItem.objects.create(
            order=self.order,
            producto=self.product,
            cantidad=3,
            precio=self.product.precio
        )

        self.assertEqual(self.order.items.count(), 1) 
        self.assertEqual(order_item.cantidad, 3)
        self.assertEqual(order_item.precio, self.product.precio)
