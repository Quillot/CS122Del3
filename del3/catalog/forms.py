from django import forms
from catalog.models import Product
from catalog.choices import COLOR_CHOICES

class ProductForm(forms.Form):
	name = forms.CharField(max_length=250, required=True, help_text='Required')
	color = forms.ChoiceField(choices=COLOR_CHOICES)
	quantity_stocked = forms.IntegerField(min_value=1, max_value=99)
	personalization_limit = forms.IntegerField(min_value=0)
	price = forms.DecimalField(decimal_places=2, max_digits=11, required=True)

	class Meta:
		model = Product
		fields = ('name', 'color', 'quantity_stocked', 'personalization_limit', 'price')