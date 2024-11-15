from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['producto']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email',
                    'dirección', 'código_postal', 'ciudad',
                    'pagado', 'creado', 'actualizado', 'entrega_en_oficina_de_correos']
    list_filter = ['pagado', 'creado', 'actualizado']
    inlines = [OrderItemInline]