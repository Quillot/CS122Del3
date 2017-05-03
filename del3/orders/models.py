from django.db import models

from agents.models import Agent
from catalog.models import Product

class Recipient(models.Model):
	recipient_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=255, blank=True, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	street = models.CharField(max_length=255, blank=True, null=True)
	city = models.CharField(max_length=255, blank=True, null=True)
	country = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.recipient_id)

	class Meta:
		app_label = 'orders'
		db_table = 'recipient'


class OrderInfo(models.Model):
	order_id = models.AutoField(primary_key=True, unique=True)
	agent_id = models.ForeignKey(Agent, db_column='agent_id', default=1)
	recipient_id = models.ForeignKey(Recipient, db_column='recipient_id', default=1)
	issue_date = models.DateField(blank=True, null=True)
	issue_time = models.TimeField(blank=True, null=True)
	delivery_date = models.DateField(blank=True, null=True)
	delivery_time = models.TimeField(blank=True, null=True)	

	def __str__(self):
		return str(self.order_id)

	class Meta:
		app_label = 'orders'
		db_table = 'orderinfo'

class Content(models.Model):
	order_id = models.ForeignKey(OrderInfo, db_column='order_id', default=1)
	product_id = models.ForeignKey(Product, db_column='product_id', default=1)
	personalization = models.CharField(max_length=255, blank=True, null=True)
	quantity_ordered = models.IntegerField(blank=True, null=True)
	discount = models.FloatField(blank=True, null=True)

	def __str__(self):
		return str(self.order_id + "|" + self.product_id)

	class Meta:
		app_label = 'orders'
		db_table = 'content'
		unique_together = (('order_id', 'product_id'),)
