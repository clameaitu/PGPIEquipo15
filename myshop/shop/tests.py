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


class SearchViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(nombre="Velas", slug="velas")
        self.product1 = Product.objects.create(
            categoria=self.category,
            nombre="Vela de Jazmín",
            slug="vela-de-jazmin",
            descripcion="Una vela aromática con esencia de jazmín.",
            precio=15.50,
            cantidad=10
        )
        self.product2 = Product.objects.create(
            categoria=self.category,
            nombre="Vela de Lavanda",
            slug="vela-de-lavanda",
            descripcion="Una vela relajante con aroma a lavanda.",
            precio=18.00,
            cantidad=5
        )

    def test_search_view_empty_query(self):
        response = self.client.get(reverse('shop:search'), {'query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/search.html')
        self.assertContains(response, "Buscar productos")
        self.assertEqual(len(response.context['results']), 0)

    def test_search_view_valid_query(self):
        response = self.client.get(reverse('shop:search'), {'query': 'jazmín'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/search.html')
        self.assertContains(response, "Vela de Jazmín")
        self.assertEqual(len(response.context['results']), 1)
        self.assertIn(self.product1, response.context['results'])

    def test_search_view_partial_match_name(self):
        response = self.client.get(reverse('shop:search'), {'query': 'Vela'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/search.html')
        self.assertContains(response, "Vela de Jazmín")
        self.assertContains(response, "Vela de Lavanda")
        self.assertEqual(len(response.context['results']), 2)

    def test_search_view_description_match_description(self):
        """Prueba la búsqueda que coincide con la descripción del producto"""
        response = self.client.get(reverse('shop:search'), {'query': 'lavanda'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/search.html')
        self.assertContains(response, "Vela de Lavanda")
        self.assertEqual(len(response.context['results']), 1)
        self.assertIn(self.product2, response.context['results'])

    def test_search_view_category_match_category(self):
        """Prueba la búsqueda que coincide con el nombre de la categoría"""
        response = self.client.get(reverse('shop:search'), {'query': 'Velas'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product/search.html')
        self.assertContains(response, "Vela de Jazmín")
        self.assertContains(response, "Vela de Lavanda")
        self.assertEqual(len(response.context['results']), 2)