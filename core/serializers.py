from rest_framework import serializers
from .models import User, Restaurant, MenuItem, Order, OrderItem, Delivery

# Serializer за User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # core.User, който наследява AbstractUser
        fields = ['id', 'username', 'email', 'is_customer', 'is_delivery', 'is_restaurant']

# Serializer за Restaurant
class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)  # Включваме детайли за собственика

    class Meta:
        model = Restaurant
        fields = ['id', 'owner', 'name', 'address']

# Serializer за MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'name', 'description', 'price']

# Serializer за Order
class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)  # Включваме детайли за клиента

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'is_delivered']

# Serializer за OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)  # Включваме детайли за продукта

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity']

# Serializer за Delivery
class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)  # Включваме детайли за поръчката
    delivery_person = UserSerializer(read_only=True)  # Включваме детайли за доставчика

    class Meta:
        model = Delivery
        fields = ['id', 'order', 'delivery_person', 'delivered_at']