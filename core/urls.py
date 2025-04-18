from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import (
    UserViewSet,
    RestaurantViewSet,
    MenuItemViewSet,
    OrderViewSet,
    OrderItemViewSet,
    DeliveryViewSet,
)

# Създаваме рутер
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'deliveries', DeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order/', views.OrderView.as_view(), name='order'),  # Нов маршрут за поръчване на храна
]