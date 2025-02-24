from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
#     path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
# ]


from django.urls import path
from .views import (
    CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    OrderItemListCreateAPIView, OrderItemRetrieveUpdateDestroyAPIView,
    PaymentListCreateAPIView, PaymentRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<str:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<str:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),

    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<str:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    path('order-items/', OrderItemListCreateAPIView.as_view(), name='orderitem-list-create'),
    path('order-items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='orderitem-detail'),

    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]



