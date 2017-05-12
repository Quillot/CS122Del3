from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import OrderInfo, Content, Delivery
from agents.models import Agent
from catalog.models import Product
from customers.models import Customer
from datetime import datetime
def index(request):
	try:
		agent = Agent.objects.get(agent_id=request.user.pk)
		order_list = OrderInfo.objects.filter(agent_id=agent)
		content_list = Content.objects.filter(order_id__in=order_list)
		delivery_list = Delivery.objects.filter(order_id__in=order_list)
		order_attribs = OrderInfo._meta.fields
		content_attribs = Content._meta.fields
		is_agent = True
		return render(request, 'orders/index.html', {'is_agent': is_agent, 'order_list': order_list, 'order_attribs': order_attribs,
		'content_list': content_list, 
		'delivery_list': delivery_list,
		'content_attribs': content_attribs})
	except Agent.DoesNotExist:
		is_agent = False
	try:
		customer = Customer.objects.get(customer_id=request.user.pk)
		order_list = OrderInfo.objects.filter(customer_id=request.user.pk)
		content_list = Content.objects.filter(order_id__in=order_list)
		delivery_list = Delivery.objects.filter(order_id__in=order_list)
	except Customer.DoesNotExist:
		order_list = OrderInfo.objects.all()
		content_list = Content.objects.all()
		delivery_list = Delivery.objects.all()
	order_attribs = OrderInfo._meta.fields
	content_attribs = Content._meta.fields
	return render(request, 'orders/index.html', {'is_agent': is_agent, 'order_list': order_list, 'order_attribs': order_attribs,
		'content_list': content_list, 
		'delivery_list': delivery_list,
		'content_attribs': content_attribs})

def approve_order(request, order_id):
	try:
		agent = Agent.objects.get(pk=request.user.id)
		order = OrderInfo.objects.get(order_id=order_id)
		content = Content.objects.filter(order_id=order.order_id)
		content_products = Content.objects.filter(order_id=order.order_id).values('product_id')
		product = Product.objects.filter(product_id__in=content_products)
		for item in content:
			if item.quantity_ordered <= item.product_id.quantity_stocked:
				all_good = True
			else:
				all_good = False
		if order.cart_ready is True and all_good is True:
			order.issue_date = datetime.today()
			order.issue_time = datetime.now().time()
			order.delivery_date = datetime.today()
			order.delivery_time = datetime.now().time()
			order.save()
			agent.total_transactions += 1
			agent.save()
			for item in content:
				product = Product.objects.get(product_id=item.product_id.pk)
				product.quantity_stocked -= item.quantity_ordered
				product.save()
			return HttpResponseRedirect(reverse('orders:index'))
		else:
			return HttpResponseRedirect(reverse('orders:index'))
	except Agent.DoesNotExist:
		return HttpResponseRedirect(reverse('orders:index'))
