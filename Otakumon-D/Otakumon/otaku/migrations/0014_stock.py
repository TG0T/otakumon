# Generated by Django 5.0.6 on 2024-06-12 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otaku', '0013_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='otaku.manga')),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
