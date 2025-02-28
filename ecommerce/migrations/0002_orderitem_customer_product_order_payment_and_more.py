# Generated by Django 5.0.12 on 2025-02-27 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_id', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_charges', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'order_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('customer_zip_code_prefix', models.IntegerField(blank=True, null=True)),
                ('customer_city', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_state', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_weight_g', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_length_cm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_height_cm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_width_cm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('order_status', models.CharField(blank=True, max_length=50, null=True)),
                ('order_purchase_timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_approved_at', models.DateTimeField(blank=True, null=True)),
                ('order_delivered_timestamp', models.DateTimeField(blank=True, null=True)),
                ('order_estimated_delivery_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce.customer')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_sequential', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_installments', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order', models.ForeignKey(db_column='order_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order')),
            ],
            options={
                'db_table': 'payments',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
