from django.test import TestCase
from django.urls import reverse
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



class OrderTrackingTests(TestCase):
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
            codigo="TESTCODE123",
            nombre="John",
            apellidos="Doe",
            email="john@example.com",
            dirección="123 Main St",
            código_postal="12345",
            ciudad="Test City",
            entrega_en_oficina_de_correos=False
        )

        self.order_item = OrderItem.objects.create(
            order=self.order,
            producto=self.product,
            cantidad=2,
            precio=self.product.precio
        )

    def test_valid_order_tracking(self):
        response = self.client.get(reverse('orders:detalles_pedido', kwargs={'codigo': self.order.codigo}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Producto de prueba")
        self.assertContains(response, "20,0")  # Precio total del producto (2 * 10.0)


    def test_order_summary_in_tracking(self):
        response = self.client.get(reverse('orders:detalles_pedido', kwargs={'codigo': self.order.codigo}))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Total: 20,0")  # Confirmar que el total del pedido aparece correctamente

    def test_search_order_by_code(self):
        response = self.client.get(reverse('orders:buscar_pedido'), {'codigo': self.order.codigo})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Producto de prueba")
        self.assertContains(response, "20,0")  # Precio total del producto