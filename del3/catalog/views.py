from django.shortcuts import render, get_object_or_404, redirect
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product, Feature
from orders.models import OrderInfo, Content
from customers.models import Customer
from agents.models import Agent

from .forms import ProductForm, AddCartForm

def index(request, product_id=None):
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
	try:
		agent = Agent.objects.get(agent_id=request.user.pk)
		is_agent=True
	except Agent.DoesNotExist:
		is_agent=False
		if not is_agent:
			try:
				customer = Customer.objects.get(customer_id=request.user.pk)
			except Customer.DoesNotExist:
				is_agent=False
	form = AddCartForm()
	return render(request, 'catalog/index.html', {'form': form,
												'is_agent': is_agent,
												'product_colors': product_colors, 
												'product_selected': product_selected, 
												'product_list': product_list, 
												'attribs': attribs,
												'feature_list': feature_list})


def add_to_cart(request, product_id):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = AddCartForm(request.POST)
			if form.is_valid():
				quantity = form.cleaned_data.get('quantity')
				personalization = form.cleaned_data.get('personalization')

				product = Product.objects.get(pk=product_id)
				curr_customer = Customer.objects.get(customer_id=request.user.id)
				orders = OrderInfo.objects.filter(customer_id=request.user.id)
				
				if len(personalization) > product.personalization_limit:
					warning = "Over personalization limit"
					product_list = Product.objects.all()
					attribs = Product._meta.fields
					return render(request, 'catalog/index.html', {'product_list': product_list, 'attribs': attribs, 'warning': warning})
			
				if quantity <= 99:
					if len(orders) == 0:  # If no current cart
						#make a new cart
						cart = create_cart(curr_customer)
						#add the product to it
						contents = insert_contents(cart, product, quantity, personalization)
						return HttpResponseRedirect(reverse('catalog:index'))
					elif len(orders) > 0:  # if there is existing cart or orders
						x = OrderInfo.objects.filter(delivery_time=None, cart_ready=False)
						y = set(orders).intersection(set(x))
						if len(y) > 0:  # if there is existing cart
							contents = insert_contents(y.pop(), product, quantity, personalization)
							return HttpResponseRedirect(reverse('catalog:index'))
						else:
							cart = create_cart(curr_customer)
							contents = insert_contents(cart, product, quantity, personalization)
							return HttpResponseRedirect(reverse('catalog:index'))
				else:
					warning = "Please choose below 99"
					product_list = Product.objects.all()
					attribs = Product._meta.fields
					return render(request, 'catalog/index.html', {'product_list': product_list, 'attribs': attribs, 'warning': warning})
			else:
				return HttpResponseRedirect(reverse('catalog:index'))
		else:
			return HttpResponseRedirect(reverse('catalog:index'))
	else:
		return HttpResponseRedirect(reverse('signup'))



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

def insert_contents(cart, product, qty, prsn):
	try:
		contents = Content.objects.get(order_id=cart, product_id=product)
		if contents.quantity_ordered + qty > 99:
			pass
		else:
			contents.quantity_ordered += qty
	except Content.DoesNotExist:
		contents = Content()
		contents.order_id = cart
		contents.product_id = product
		contents.quantity_ordered = qty
		contents.discount = 0.00
	contents.personalization = prsn
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
