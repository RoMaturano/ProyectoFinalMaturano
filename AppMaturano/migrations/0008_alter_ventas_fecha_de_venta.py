# Generated by Django 4.1.3 on 2022-12-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMaturano', '0007_rename_monto_comprador_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='fecha_de_venta',
            field=models.DateField(),
        ),
    ]