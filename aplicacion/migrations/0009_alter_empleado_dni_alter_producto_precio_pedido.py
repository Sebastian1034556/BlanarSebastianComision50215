# Generated by Django 5.0.2 on 2024-03-25 21:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_avatar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='dni',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('productos', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]