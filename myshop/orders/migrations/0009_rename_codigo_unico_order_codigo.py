# Generated by Django 5.1.3 on 2024-11-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0008_order_codigo_unico"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order", old_name="codigo_unico", new_name="codigo",
        ),
    ]
