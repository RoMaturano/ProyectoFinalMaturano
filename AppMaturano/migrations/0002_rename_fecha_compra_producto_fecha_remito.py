# Generated by Django 4.1.3 on 2022-12-01 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMaturano', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='fecha_compra',
            new_name='fecha_remito',
        ),
    ]