from django.contrib import admin
from django.contrib import admin
from .models import Customer, Order, Product, OrderItem, Payment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id","customer_zip_code_prefix", "customer_city", "customer_state")
    search_fields = ("customer_id", "customer_city")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #list_display = ("order_id", "customer_display", "order_status", "order_purchaorder_idse_timestamp, order_approved_at, order_delivered_timestamp, order_estimated_delivery_date")
    
    list_display = [
    'order_id',
    'customer_display',
    'order_status',
    'order_purchase_timestamp', 
    'order_approved_at', 
    'order_delivered_timestamp', 
    'order_estimated_delivery_date'
    ]

    search_fields = ("order_id", "customer__customer_id")

    def customer_display(self, obj):
        return obj.customer.customer_id if obj.customer else "N/A"
    customer_display.short_description = "Customer"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    #list_display = ("product_id", "product_category_name", "product_weight_g, product_length_cm, product_height_cm, product_width_cm")

    list_display = [
    'product_id', 
    'product_category_name', 
    'product_weight_g', 
    'product_length_cm', 
    'product_height_cm', 
    'product_width_cm'
    ]

    search_fields = ("product_id", "product_category_name")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order_item_id", "order_display", "product_display", "seller_id", "price", "shipping_charges")
    search_fields = ("order__order_id", "product__product_id")

    def order_display(self, obj):
        return obj.order.order_id if obj.order else "N/A"
    order_display.short_description = "Order"

    def product_display(self, obj):
        return obj.product.product_id if obj.product else "N/A"
    product_display.short_description = "Product"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order_display", "payment_sequential", "payment_type", "payment_value", "payment_installments")
    search_fields = ("order__order_id", "payment_type")

    def order_display(self, obj):
        return obj.order.order_id if obj.order else "N/A"
    order_display.short_description = "Order"
