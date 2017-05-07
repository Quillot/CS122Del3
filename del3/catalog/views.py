from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import Product
from orders.models import OrderInfo, Content
from customers.models import Customer

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

	product.quantity_stocked -= 10
	product.save()

	return contents

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
