from django.shortcuts import render, get_object_or_404
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product, Feature
from orders.models import OrderInfo, Content
from customers.models import Customer

from .forms import ProductForm

def index(request):
	product_list = Product.objects.all()
	product_selected = Product.objects.all().values('name').distinct()
	product_colors = {}
	feature_list = Feature.objects.all()
	for product in product_selected:
		colors = []
		for pr in Product.objects.filter(name=product["name"]):
			colors.append(pr.color)
		product_colors[product["name"]] = colors
	attribs = Product._meta.fields
	return render(request, 'catalog/index.html', {'product_colors': product_colors, 
												'product_selected': product_selected, 
												'product_list': product_list, 
												'attribs': attribs,
												'feature_list': feature_list})

def add_to_cart(request, product_id):
	if request.user.is_authenticated():
		product = Product.objects.get(pk=product_id)
		curr_customer = Customer.objects.get(customer_id=request.user.id)
		orders = OrderInfo.objects.filter(customer_id=request.user.id)
		if product.quantity_stocked > 10:
			if len(orders) == 0:  # If no current cart
				#make a new cart
				cart = create_cart(curr_customer)
				#add the product to it
				contents = insert_contents(cart, product)
				return HttpResponseRedirect(reverse('catalog:index'))
			elif len(orders) > 0:  # if there is existing cart or orders
				x = OrderInfo.objects.filter(delivery_time=None, cart_ready=False)
				y = set(orders).intersection(set(x))
				if len(y) > 0:  # if there is existing cart
					contents = insert_contents(y.pop(), product)
					return HttpResponseRedirect(reverse('catalog:index'))
				else:
					cart = create_cart(curr_customer)
					contents = insert_contents(cart, product)
					return HttpResponseRedirect(reverse('catalog:index'))
		else:
			warning = "Not enough stock"
			product_list = Product.objects.all()
			attribs = Product._meta.fields
			return render(request, 'catalog/index.html', {'product_list': product_list, 'attribs': attribs, 'warning': warning})
	else:
		#if not authenticated
		return HttpResponseRedirect(reverse('catalog:index'))

def create_cart(customer):
	cart = OrderInfo()
	cart.agent_id = customer.agent_id
	cart.customer_id = customer
	cart.issue_date = None
	cart.issue_time = None
	cart.delivery_date = None
	cart.delivery_time = None
	cart.save()
	return cart

def insert_contents(cart, product):
	try:
		contents = Content.objects.get(order_id=cart, product_id=product)
		contents.quantity_ordered += 10
	except Content.DoesNotExist:
		contents = Content()
		contents.order_id = cart
		contents.product_id = product
		contents.personalization = 'test'
		contents.quantity_ordered = 10
		contents.discount = 0.00
	contents.save()

	# product.quantity_stocked -= 10
	# product.save()

	return contents

def add_product(request):
	if request.user.is_staff:
		if request.method == 'POST':
			form = ProductForm(request.POST)
			if form.is_valid():
				product = form.save()
				features = form.cleaned_data.get('features')
				for feature in features.splitlines():
					Feature(product_id=product, feature_desc=feature.strip()).save()
				return HttpResponseRedirect(reverse('catalog:index'))
			else:
				return render(request, 'catalog/addproduct.html', {'form': form})
		else: 
			form = ProductForm()
			return render(request, 'catalog/addproduct.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('catalog:index'))


@staff_member_required
def delete_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	product.delete()
	return HttpResponseRedirect(reverse('catalog:index'))
