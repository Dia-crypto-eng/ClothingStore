# Generated by Django 5.0.1 on 2024-04-11 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_id_product_idproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]