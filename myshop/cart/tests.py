from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product


class CartViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            nombre="Perfumes",
            slug="perfumes"
        )
        self.product = Product.objects.create(
            categoria=self.category,
            nombre="Perfume de Rosas",
            slug="perfume-de-rosas",
            precio=29.99,
            cantidad=15
        )

    def test_cart_add_view(self):
        response = self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'cantidad': 2, 'override': False}
        )
        self.assertEqual(response.status_code, 302)  # Redirección a cart_detail
        self.assertRedirects(response, reverse('cart:cart_detail'))

        # Comprobar que el producto ha sido añadido al carrito
        session = self.client.session
        cart = session.get('cart')
        self.assertIsNotNone(cart)
        self.assertIn(str(self.product.id), cart)
        self.assertEqual(cart[str(self.product.id)]['quantity'], 2)

    def test_cart_remove_view(self):
        self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'cantidad': 2, 'override': False}
        )
        
        response = self.client.post(
            reverse('cart:cart_remove', args=[self.product.id])
        )
        self.assertEqual(response.status_code, 302)  # Redirección a cart_detail
        self.assertRedirects(response, reverse('cart:cart_detail'))

        # Comprobar que el producto ha sido eliminado del carrito.
        session = self.client.session
        cart = session.get('cart')
        self.assertIsNotNone(cart)
        self.assertNotIn(str(self.product.id), cart)

    def test_cart_detail_view(self):
        self.client.post(
            reverse('cart:cart_add', args=[self.product.id]),
            {'cantidad': 1, 'override': False}
        )

        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/detail.html')
        self.assertContains(response, "Perfume de Rosas")
        self.assertContains(response, "29,99")

