# Generated by Django 3.1.8 on 2025-02-23 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('customer_zip_code_prefix', models.IntegerField()),
                ('customer_city', models.CharField(max_length=255)),
                ('customer_state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('order_status', models.CharField(max_length=50)),
                ('order_purchase_timestamp', models.DateTimeField(auto_now_add=True)),
                ('order_approved_at', models.DateTimeField(blank=True, null=True)),
                ('order_delivered_timestamp', models.DateTimeField(blank=True, null=True)),
                ('order_estimated_delivery_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('seller_id', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shipping_charges', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=50)),
                ('payment_installments', models.IntegerField(default=1)),
                ('payment_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(max_length=255)),
                ('product_weight_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_length_cm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_height_cm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_width_cm', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='ecommerce.product'),
        ),
    ]
