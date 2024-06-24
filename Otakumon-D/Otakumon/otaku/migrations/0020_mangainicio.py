# Generated by Django 5.0.6 on 2024-06-24 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otaku', '0019_remove_manga_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MangaInicio',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('sub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otaku.manga')),
            ],
        ),
    ]
