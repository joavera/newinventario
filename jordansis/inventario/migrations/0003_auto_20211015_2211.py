# Generated by Django 3.2.7 on 2021-10-16 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20211015_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='ventadetalleproductos',
        ),
        migrations.RemoveField(
            model_name='notas',
            name='ventadetalleventatienda',
        ),
    ]
