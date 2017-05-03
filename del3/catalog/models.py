from django.db import models
from catalog.choices import COLOR_CHOICES

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, blank=True, null=True)
	color = models.CharField(choices=COLOR_CHOICES, max_length=255, blank=True, null=True)
	quantity_stocked = models.IntegerField(blank=True, null=True)
	personalization_limit = models.IntegerField(blank=True, null=True)
	price = models.FloatField(blank=True, null=True)

	def __str__(self):
		return str(self.product_id)

	class Meta:
		app_label = 'catalog'
		db_table = 'product'