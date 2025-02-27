from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    customer_zip_code_prefix = models.IntegerField(null=True, blank=True)
    customer_city = models.CharField(max_length=255, null=True, blank=True)
    customer_state = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return f"ID: {self.customer_id} | Zip: {self.customer_zip_code_prefix} | City: {self.customer_city} | State: {self.customer_state}"


class Order(models.Model):
    order_id = models.CharField(max_length=255, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", null=True, blank=True)
    order_status = models.CharField(max_length=50, null=True, blank=True)
    order_purchase_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order_approved_at = models.DateTimeField(null=True, blank=True)
    order_delivered_timestamp = models.DateTimeField(null=True, blank=True)
    order_estimated_delivery_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f"Order ID: {self.order_id} | Status: {self.order_status} | Customer: {self.customer.customer_id if self.customer else 'N/A'} | Purchase Date: {self.order_purchase_timestamp}"


class Product(models.Model):
    product_id = models.CharField(max_length=255, primary_key=True)
    product_category_name = models.CharField(max_length=255, null=True, blank=True)
    product_weight_g = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_length_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_height_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_width_cm = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "products"

    def __str__(self):
        return f"ID: {self.product_id} | Category: {self.product_category_name} | Weight: {self.product_weight_g}g | Dimensions: {self.product_length_cm}x{self.product_width_cm}x{self.product_height_cm} cm"


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='order_items',
        db_column='order_id', null=True, blank=True
    )
    
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='order_items',
        db_column='product_id', null=True, blank=True
    )
    seller_id = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)

    class Meta:
        db_table = "order_items"
        managed = False

    def __str__(self):
        return f"Order Item ID: {self.order_item_id} | Order: {self.order.order_id if self.order else 'N/A'} | Product: {self.product.product_id if self.product else 'N/A'} | Seller: {self.seller_id} | Price: {self.price} | Shipping: {self.shipping_charges}"


class Payment(models.Model):
    id = models.AutoField(primary_key=True)

    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        to_field="order_id",
        db_column="order_id",
        null=True,
    )
    payment_sequential = models.CharField(max_length=50, null=True, blank=True)
    payment_type = models.CharField(max_length=50, null=True, blank=True)
    payment_installments = models.CharField(max_length=50, null=True, blank=True)
    payment_value = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = "payments"
        managed = True 

    def __str__(self):
        return f"Payment ID: {self.id} | Order: {self.order.order_id if self.order else 'N/A'} | Type: {self.payment_type} | Installments: {self.payment_installments} | Value: {self.payment_value}"
