# Generated by Django 5.1.3 on 2024-11-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_product_cantidad_alter_product_disponible"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("nombre",),
                "verbose_name": "categoría",
                "verbose_name_plural": "categorías",
            },
        ),
    ]
