# from rest_framework import serializers
# from .models import Movie
# from django.contrib.auth.models import User


# class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
#     creator = serializers.ReadOnlyField(source='creator.username')

#     class Meta:
#         model = Movie
#         fields = ('id', 'title', 'genre', 'year', 'creator')


# class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
#     movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'movies')

from rest_framework import serializers
from .models import Customer, Order, Product, OrderItem, Payment


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
