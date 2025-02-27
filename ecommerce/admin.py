from django.contrib import admin
from django.contrib import admin
from .models import Customer, Order, Product, OrderItem, Payment

#admin.site.register(Customer)
#admin.site.register(Order)
#admin.site.register(Product)
#admin.site.register(OrderItem)
#admin.site.register(Payment)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "customer_city", "customer_state")
    search_fields = ("customer_id", "customer_city", "customer_state")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "customer", "order_status", "order_purchase_timestamp")
    search_fields = ("order_id", "customer__customer_id", "order_status")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", "product_category_name", "product_weight_g")
    search_fields = ("product_id", "product_category_name")

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order_item_id", "order", "product", "seller_id", "price")
    search_fields = ("order__order_id", "product__product_id", "seller_id")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "payment_type", "payment_value")
    search_fields = ("order__order_id", "payment_type", "payment_value")

