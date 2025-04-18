from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Разширен потребител
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'is_restaurant': True})
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}"

# Артикул в поръчка (много към много)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

# Доставка
class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_person = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_delivery': True})
    delivered_at = models.DateTimeField(null=True, blank=True)
