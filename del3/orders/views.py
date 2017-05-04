from django.shortcuts import render

from .models import OrderInfo, Content, Delivery

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def index(request):
	order_list = OrderInfo.objects.all()
	attribs = OrderInfo._meta.fields
	content_list = Content.objects.all()
	delivery_list = Delivery.objects.all()
	return render(request, 'orders/index.html', {'order_list': order_list, 'attribs': attribs, 'content_list': content_list, 'delivery_list': delivery_list})