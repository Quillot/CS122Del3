from django import forms
from catalog.models import Product, Feature
from catalog.choices import COLOR_CHOICES

class ProductForm(forms.Form):
	name = forms.CharField(max_length=250, required=True, help_text='Required')
	color = forms.ChoiceField(choices=COLOR_CHOICES)
	quantity_stocked = forms.IntegerField(min_value=1, max_value=99)
	personalization_limit = forms.IntegerField(min_value=0)
	price = forms.DecimalField(decimal_places=2, max_digits=11, required=True)
	features = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Product
		fields = ('name', 'color', 'quantity_stocked', 'personalization_limit', 'price')


	def save(self, commit=False):
		try:
			product = Product.objects.get(name=self.cleaned_data.get('name').title(), color = self.cleaned_data.get('color'))
			return product
		except Product.DoesNotExist:
			product = Product()
		product.name = self.cleaned_data.get('name').title()
		product.color = self.cleaned_data.get('color')
		product.quantity_stocked = self.cleaned_data.get('quantity_stocked')
		product.personalization_limit = self.cleaned_data.get('personalization_limit')
		product.price = self.cleaned_data.get('price')
		features = self.cleaned_data.get('features')
		product.save()
		for feature in features.splitlines():
			Feature(product_id=product, feature_desc=feature.strip()).save()
		return product

class AddCartForm(forms.Form):
	quantity = forms.IntegerField(min_value = 1, max_value=99)
	personalization = forms.CharField(max_length=255, required=False)

	class Meta:
		model = Product
		fields = ('quantity', 'personalization')