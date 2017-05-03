from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product

from .forms import ProductForm

def index(request):
	if request.method == 'POST':
		if request.user.is_staff: 
			form = ProductForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data.get('name')
				color = form.cleaned_data.get('color')
				quantity_stocked = form.cleaned_data.get('quantity_stocked')
				personalization_limit = form.cleaned_data.get('personalization_limit')
				price = form.cleaned_data.get('price')
				product = Product()
				product.name = name
				product.color = color
				product.quantity_stocked = quantity_stocked
				product.personalization_limit = personalization_limit
				product.price = price
				product.save()
				return HttpResponseRedirect(reverse('catalog:index'))
		else:
			return HttpResponse('Not allowed to add product')
	product_list = Product.objects.all()
	attribs = Product._meta.fields
	return render(request, 'catalog/index.html', {'product_list': product_list, 'attribs': attribs})

@staff_member_required
def add_product(request):
	if request.user.is_staff:
		form = ProductForm()
		return render(request, 'catalog/addproduct.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('catalog:index'))

@staff_member_required
def delete_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	product.delete()
	return HttpResponseRedirect(reverse('catalog:index'))
