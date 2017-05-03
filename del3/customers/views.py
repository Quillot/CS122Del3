from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import Customer

@staff_member_required
def index(request):
	customer_list = Customer.objects.all()
	attribs = Customer._meta.fields
	return render(request, 'customers/index.html', {'customer_list': customer_list, 'attribs': attribs})