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
		if len(orders) == 0:  # If no current cart
			#make a new cart
			cart = OrderInfo()
			cart.agent_id = curr_customer.agent_id
			cart.customer_id = curr_customer
			cart.issue_date = None
			cart.issue_time = None
			cart.delivery_date = None
			cart.delivery_time = None
			cart.save()

			#add the product to it
			contents = Content()
			contents.order_id = cart
			contents.product_id = product
			contents.personalization = 'test'
			contents.quantity_stocked = 10
			contents.discount = 0.00
			contents.save()
			return HttpResponseRedirect(reverse('catalog:index'))
		elif len(orders) > 0:  # if there is existing cart or orders
			for order in orders:
				if order.delivery_date is not None:  # if already delivered
					return HttpResponse('Already delivered, make a new cart')
				elif order.delivery_date is None:  # if still a cart
					#add the product to cart
					contents = Content()
					contents.order_id = order
					contents.product_id = product
					contents.personalization = 'test'
					contents.quantity_stocked = 10
					contents.discount = 0.00
					contents.save()
					return HttpResponseRedirect(reverse('catalog:index'))
				else: pass
			return HttpResponse('test')
	else:
		#if not authenticated
		return HttpResponseRedirect(reverse('catalog:index'))


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
