# Generated by Django 5.0.2 on 2024-08-06 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0023_remove_pedido_cantidad_alter_pedido_direccion"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="productos",
        ),
    ]
