# Generated by Django 5.1.3 on 2024-11-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_entrega_en_oficina_de_correos'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fecha_salida_almacen',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='notas_seguimiento',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='recibido_correctamente',
            field=models.BooleanField(default=False),
        ),
    ]
