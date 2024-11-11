# Generated by Django 5.1.3 on 2024-11-11 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("nombre",),
                "verbose_name": "categoria",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="product", options={"ordering": ("nombre",)},
        ),
        migrations.RenameField(
            model_name="category", old_name="name", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="product", old_name="updated", new_name="actualizado",
        ),
        migrations.RenameField(
            model_name="product", old_name="category", new_name="categoria",
        ),
        migrations.RenameField(
            model_name="product", old_name="created", new_name="creado",
        ),
        migrations.RenameField(
            model_name="product", old_name="description", new_name="descripcion",
        ),
        migrations.RenameField(
            model_name="product", old_name="available", new_name="disponible",
        ),
        migrations.RenameField(
            model_name="product", old_name="image", new_name="imagen",
        ),
        migrations.RenameField(
            model_name="product", old_name="name", new_name="nombre",
        ),
        migrations.RenameField(
            model_name="product", old_name="price", new_name="precio",
        ),
    ]
