# Generated by Django 5.0.1 on 2024-08-23 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0010_alter_invoiceitem_invoice_alter_invoiceitem_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('ClientID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(default='', max_length=50)),
                ('LastName', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('PhoneNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('CompanyID', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(default='', max_length=50)),
                ('CRN', models.CharField(default='', max_length=25)),
                ('NIS', models.CharField(default='', max_length=25)),
                ('NIF', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ClientCompanyLinks',
            fields=[
                ('LinkID', models.AutoField(primary_key=True, serialize=False)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.clients')),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentMethod', models.CharField(choices=[('fundtransfer', 'Fund Transfer'), ('check', 'Check'), ('cash', 'Cash')], default='cash', max_length=20)),
                ('AmountPaid', models.FloatField(default=0)),
                ('PaymentDate', models.DateField(default=0)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.clients')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInvoiceLink',
            fields=[
                ('link_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_payment', models.CharField(choices=[('payment', 'Payment'), ('invoice', 'Invoice')], max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clients')),
                ('related_invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
                ('related_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.payments')),
            ],
        ),
    ]