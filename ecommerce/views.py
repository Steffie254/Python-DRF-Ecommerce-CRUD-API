# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
# from rest_framework.permissions import IsAuthenticated
# from django_filters import rest_framework as filters
# from .models import Movie
# from .permissions import IsOwnerOrReadOnly
# from .serializers import MovieSerializer
# from .pagination import CustomPagination
# from .filters import MovieFilter


# class ListCreateMovieAPIView(ListCreateAPIView):
#     serializer_class = MovieSerializer
#     queryset = Movie.objects.all()
#     permission_classes = [IsAuthenticated]
#     pagination_class = CustomPagination
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = MovieFilter

#     def perform_create(self, serializer):
#         # Assign the user who created the movie
#         serializer.save(creator=self.request.user)


# class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = MovieSerializer
#     queryset = Movie.objects.all()
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order, Product, OrderItem, Payment
from .serializers import (
    CustomerSerializer, OrderSerializer, ProductSerializer,
    OrderItemSerializer, PaymentSerializer
)


class CustomerListCreateAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class OrderItemListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]


class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]


