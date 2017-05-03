from django.db import models
from django.contrib.auth.models import User

from agents.models import Agent

class Customer(models.Model):
	customer_id = models.OneToOneField(User, db_column='customer_id', primary_key=True)
	agent_id = models.ForeignKey(Agent, db_column='agent_id', null=False,default=2)
	street = models.CharField(max_length=255, blank=False, null=False, default='Shiny Street')
	city = models.CharField(max_length=255, blank=False, null=False, default='Clean City')
	country = models.CharField(max_length=255, blank=False, null=False, default='Cool Country')

	class Meta:
		app_label = 'customers'
		db_table = 'customer'

	def __str__(self):
		return str(self.customer_id)

