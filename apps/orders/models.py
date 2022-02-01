import uuid
from django.db import models

from apps.products.models import Product
from apps.users.models import EUser


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.ForeignKey(EUser, related_name='orders', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	
	class Meta:
		ordering = ['-created_at', ]
	
	def __str__(self):
		return self.first_name


class OrderItem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField(default=1)
	
	def __str__(self):
		return f'{self.id}'
