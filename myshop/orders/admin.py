from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['producto']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email',
                    'dirección', 'código_postal', 'ciudad',
                    'pagado', 'creado', 'actualizado', 'entrega_en_oficina_de_correos', 
                    'fecha_salida_almacen', 'recibido_correctamente', 'notas_seguimiento']
    list_filter = ['pagado', 'creado', 'actualizado', 'recibido_correctamente']
    search_fields = ('nombre', 'apellidos', 'email', 'direccion')
    date_hierarchy = 'creado'

    list_editable = ('fecha_salida_almacen', 'recibido_correctamente','notas_seguimiento')