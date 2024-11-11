from django.db import models
from django.db.models import Index
from django.urls import reverse


class Category(models.Model):
    nombre = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    class Meta:
        ordering = ('nombre',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    categoria = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('nombre',)
        indexes = [
            Index(fields=['id', 'slug']),
        ]
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])