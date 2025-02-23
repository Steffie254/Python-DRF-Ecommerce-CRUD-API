# from django.db import models


# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     year = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['-id']


from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=255, primary_key=True)
    customer_zip_code_prefix = models.IntegerField()
    customer_city = models.CharField(max_length=255)
    customer_state = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_id


class Order(models.Model):
    order_id = models.CharField(max_length=255, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    order_status = models.CharField(max_length=50)
    order_purchase_timestamp = models.DateTimeField(auto_now_add=True)
    order_approved_at = models.DateTimeField(null=True, blank=True)
    order_delivered_timestamp = models.DateTimeField(null=True, blank=True)
    order_estimated_delivery_date = models.DateField()

    def __str__(self):
        return self.order_id


class Product(models.Model):
    product_id = models.CharField(max_length=255, primary_key=True)
    product_category_name = models.CharField(max_length=255)
    product_weight_g = models.DecimalField(max_digits=10, decimal_places=2)
    product_length_cm = models.DecimalField(max_digits=10, decimal_places=2)
    product_height_cm = models.DecimalField(max_digits=10, decimal_places=2)
    product_width_cm = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_id


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    seller_id = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.order.order_id} - {self.product.product_id}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    payment_type = models.CharField(max_length=50)
    payment_installments = models.IntegerField(default=1)
    payment_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment {self.payment_id} for Order {self.order.order_id}"
