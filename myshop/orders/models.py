from django.db import models
from shop.models import Product


class Order(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    dirección = models.CharField(max_length=250)
    código_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    entrega_en_oficina_de_correos = models.BooleanField(default=False)
    pagado = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    
    class Meta:
        ordering = ('-creado',)
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        total_cost =  sum(item.get_cost() for item in self.items.all())
        GASTOS_DE_ENVÍO = 7
        if (total_cost < 50): total_cost += GASTOS_DE_ENVÍO
        return total_cost
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    producto = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)
    
    class Meta:
        verbose_name = 'artículo pedido'
        verbose_name_plural = 'artículos pedido'
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.precio * self.cantidad