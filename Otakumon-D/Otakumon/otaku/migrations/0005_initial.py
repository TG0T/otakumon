# Generated by Django 5.0.6 on 2024-06-12 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otaku', '0004_remove_manga_autor_remove_manga_editorial_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('volumen', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otaku.autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otaku.editorial')),
            ],
        ),
    ]