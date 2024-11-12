from django.test import TestCase
from .models import Category, Product
from django.urls import reverse


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(
            nombre="Aromaterapia",
            slug="aromaterapia"
        )
        self.assertEqual(category.nombre, "Aromaterapia")
        self.assertEqual(category.slug, "aromaterapia")
        self.assertEqual(str(category), "Aromaterapia")

    def test_category_absolute_url(self):
        category = Category.objects.create(
            nombre="Herbolario",
            slug="herbolario"
        )
        self.assertEqual(
            category.get_absolute_url(), 
            f"/{category.slug}/"
        )


class ProductModelTest(TestCase):
    def test_create_product(self):
        category = Category.objects.create(
            nombre="Velas",
            slug="velas"
        )
        product = Product.objects.create(
            categoria=category,
            nombre="Vela de Canela",
            slug="vela-de-canela",
            precio=12.99,
            cantidad=15
        )
        self.assertEqual(product.nombre, "Vela de Canela")
        self.assertTrue(product.disponible)
        self.assertEqual(str(product), "Vela de Canela")

    def test_product_absolute_url(self):
        category = Category.objects.create(
            nombre="Colonias",
            slug="colonias"
        )
        product = Product.objects.create(
            categoria=category,
            nombre="Colonia de Lavanda",
            slug="colonia-de-lavanda",
            precio=25.50,
            cantidad=8
        )
        self.assertEqual(
            product.get_absolute_url(), 
            f"/{product.id}/{product.slug}/"
        )


class ProductListViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            nombre="Inciensos",
            slug="inciensos"
        )
        self.product1 = Product.objects.create(
            categoria=self.category,
            nombre="Incienso de Sándalo",
            slug="incienso-de-sandalo",
            precio=5.99,
            cantidad=10
        )
        self.product2 = Product.objects.create(
            categoria=self.category,
            nombre="Incienso de Lavanda",
            slug="incienso-de-lavanda",
            precio=6.99,
            cantidad=5
        )

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')
        self.assertContains(response, "Incienso de Sándalo")
        self.assertContains(response, "Incienso de Lavanda")

    def test_product_list_by_category_view(self):
        response = self.client.get(reverse('shop:product_list_by_category', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/list.html')
        self.assertContains(response, "Incienso de Sándalo")
        self.assertContains(response, "Incienso de Lavanda")


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            nombre="Velas",
            slug="velas"
        )
        self.product = Product.objects.create(
            categoria=self.category,
            nombre="Vela de Jazmín",
            slug="vela-de-jazmin",
            precio=15.50,
            cantidad=7
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', args=[self.product.id, self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/detail.html')
        self.assertContains(response, "Vela de Jazmín")
        self.assertContains(response, "15,50")
