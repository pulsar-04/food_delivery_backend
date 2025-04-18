from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Restaurant, MenuItem, Order, OrderItem, Delivery
from .serializers import UserSerializer, RestaurantSerializer, MenuItemSerializer, OrderSerializer, OrderItemSerializer, DeliverySerializer

# Create your views here.

# ViewSet за User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# ViewSet за Restaurant
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

# ViewSet за MenuItem
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# ViewSet за Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
# ViewSet за OrderItem
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# ViewSet за Delivery
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class OrderView(APIView):
     #permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurants = Restaurant.objects.all()
        menu_items = MenuItem.objects.all()
        return render(request, 'order.html', {
            'restaurants': restaurants,
            'menu_items': menu_items,
        })

class HomeView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/order/')
        return render(request, 'login.html')
