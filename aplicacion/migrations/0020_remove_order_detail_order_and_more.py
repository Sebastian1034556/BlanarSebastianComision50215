# Generated by Django 5.0.2 on 2024-08-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0019_alter_producto_cantidad"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order_detail",
            name="order",
        ),
        migrations.RemoveField(
            model_name="order_detail",
            name="product",
        ),
        migrations.RenameField(
            model_name="pedido",
            old_name="ubicacion",
            new_name="direccion",
        ),
        migrations.AddField(
            model_name="pedido",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="producto",
            name="cantidad",
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="Order_Detail",
        ),
    ]
