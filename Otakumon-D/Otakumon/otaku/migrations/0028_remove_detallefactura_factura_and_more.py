# Generated by Django 5.0.6 on 2024-07-03 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otaku', '0027_factura_detallefactura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='factura',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='manga',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='DetalleFactura',
        ),
    ]