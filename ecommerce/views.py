from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, Order, Product, OrderItem, Payment
from .serializers import (
    CustomerSerializer, OrderSerializer, ProductSerializer,
    OrderItemSerializer, PaymentSerializer
)


# Custom pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Default items per page
    page_size_query_param = 'page_size'  # Allows user to specify page size
    max_page_size = 100  # Maximum limit


class CustomerListCreateAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['customer_id', 'customer_city', 'customer_state']


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['order_id', 'order_status', 'customer__customer_id']


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['product_id', 'product_category_name']


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class OrderItemListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['order__order_id', 'product__product_id', 'seller_id']


class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['order__order_id', 'payment_type', 'payment_sequential']


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
