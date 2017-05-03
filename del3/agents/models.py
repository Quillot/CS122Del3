from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
	agent_id = models.OneToOneField(User, db_column='agent_id', primary_key=True)
	total_transactions = models.PositiveIntegerField(blank=False, null=False, default=0)

	class Meta:
		app_label = 'agents'
		db_table = 'agent'

	def __str__(self):
		return str(self.agent_id)

