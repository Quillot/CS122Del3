from django.db import models

from agents.models import Agent
from catalog.models import Product
from customers.models import Customer

class Recipient(models.Model):
	recipient_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=False, null=False, default='Ruscie')
	last_name = models.CharField(max_length=255, blank=False, null=False, default='Pient')
	street = models.CharField(max_length=255, blank=False, null=False, default='Shiny Street')
	city = models.CharField(max_length=255, blank=False, null=False, default='Clean City')
	country = models.CharField(max_length=255, blank=False, null=False, default='Cool Country')

	def __str__(self):
		return str(self.recipient_id)

	class Meta:
		app_label = 'orders'
		db_table = 'recipient'


class OrderInfo(models.Model):
	order_id = models.AutoField(primary_key=True, unique=True)
	agent_id = models.ForeignKey(Agent, db_column='agent_id', null=False, blank=False, default=2)
	customer_id = models.ForeignKey(Customer, db_column='customer_id', null=False, blank=False, default=4)
	issue_date = models.DateField(blank=False, null=False, default='2017-01-01')
	issue_time = models.TimeField(blank=False, null=False, default='12:00:00')
	delivery_date = models.DateField(blank=False, null=False, default='2017-01-01')
	delivery_time = models.TimeField(blank=False, null=False, default='12:00:00')	
	cart_ready = models.BooleanField(blank=False, null=False, default=0)

	def __str__(self):
		return str(self.order_id)

	class Meta:
		app_label = 'orders'
		db_table = 'orderinfo'

class Content(models.Model):
	content_id = models.AutoField(primary_key=True, unique=True)
	order_id = models.ForeignKey(OrderInfo, db_column='order_id')
	product_id = models.ForeignKey(Product, db_column='product_id')
	personalization = models.CharField(max_length=255, blank=False, null=False, default='')
	quantity_ordered = models.PositiveIntegerField(blank=False, null=False, default=1)
	discount = models.FloatField(blank=False, null=False, default=0.00)

	def __str__(self):
		return str(self.content_id)

	class Meta:
		app_label = 'orders'
		db_table = 'content'

class Delivery(models.Model):
	delivery_id = models.AutoField(primary_key=True, unique=True)
	order_id = models.OneToOneField(OrderInfo, db_column='order_id', unique=True)
	recipient_id = models.ForeignKey(Recipient, db_column='recipient_id', null=True, blank=False, default=None)
	gift = models.BooleanField(blank=False, null=False, default=0)

	def __str__(self):
		return str(self.delivery_id)

	class Meta:
		app_label = 'orders'
		db_table = 'delivery'