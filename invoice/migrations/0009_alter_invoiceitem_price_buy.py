# Generated by Django 5.0.1 on 2024-03-24 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_rename_idinvoiceelement_invoiceitem_idinvoiceelement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='price_buy',
            field=models.FloatField(default=0),
        ),
    ]