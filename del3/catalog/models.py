from django.db import models
from catalog.choices import COLOR_CHOICES

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255, blank=False, null=False, default='Swiffer')
	color = models.CharField(choices=COLOR_CHOICES, max_length=255, blank=False, null=False, default='red')
	quantity_stocked = models.PositiveIntegerField(blank=False, null=False, default=1)
	personalization_limit = models.IntegerField(blank=False, null=False, default=8)
	price = models.FloatField(blank=False, null=False, default=20.00)

	def __str__(self):
		return str(self.product_id)

	class Meta:
		app_label = 'catalog'
		db_table = 'product'

class Feature(models.Model):
	product_id = models.ForeignKey(Product, primary_key=True, null=False, default=1)
	feature_desc = models.CharField(max_length=255, blank=False, null=False, default='')

	class Meta:
		app_label = 'catalog'
		db_table = 'feature'
