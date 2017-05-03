from django.db import models

class Invite(models.Model):
	invite_code = models.IntegerField(blank=True, default=11111, primary_key=True)
	used = models.BooleanField(blank=True, default=False)

	class Meta:
		app_label = 'del3'
		db_table ='invite'