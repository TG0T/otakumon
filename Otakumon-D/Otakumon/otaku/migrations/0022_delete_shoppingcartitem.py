# Generated by Django 5.0.6 on 2024-07-03 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otaku', '0021_shoppingcartitem_delete_mangainicio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoppingCartItem',
        ),
    ]