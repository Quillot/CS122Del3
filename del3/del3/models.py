from django.db import models

class Invite(models.Model):
	invite_id = models.AutoField(primary_key=True)
	invite_code = models.IntegerField(blank=False, null=False, default=111)
	used = models.BooleanField(blank=False, null=False, default=0)

	class Meta:
		app_label = 'del3'
		db_table ='invite'

	def __str__(self):
		return str(self.invite_id)