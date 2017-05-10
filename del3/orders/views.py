from django.shortcuts import render, redirect

from .models import OrderInfo, Content, Delivery
from agents.models import Agent
from customers.models import Customer

def index(request):
	try:
		customer = Customer.objects.get(customer_id=request.user.pk)
		order_list = OrderInfo.objects.filter(customer_id=request.user.pk)
		content_list = Content.objects.filter(order_id__in=order_list)
		delivery_list = Delivery.objects.filter(order_id__in=order_list)
	except (Customer.DoesNotExist) as e:
		order_list = OrderInfo.objects.all()
		content_list = Content.objects.all()
		delivery_list = Delivery.objects.all()
	order_attribs = OrderInfo._meta.fields
	content_attribs = Content._meta.fields
	return render(request, 'orders/index.html', {'order_list': order_list, 'order_attribs': order_attribs,
		'content_list': content_list, 
		'delivery_list': delivery_list,
		'content_attribs': content_attribs})