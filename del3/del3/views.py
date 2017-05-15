from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User

from customers.models import Customer
from agents.models import Agent
from orders.models import OrderInfo, Content, Delivery, Recipient

from .forms import SignUpForm, LoginForm, SignUpAgentForm, CartForm

def index(request):
	customer_list = Customer.objects.all()
	agent_list = Agent.objects.all()
	return render(request, 'del3/index.html', {'customer_list': customer_list, 'agent_list': agent_list})

def signup(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.save()
				password=form.cleaned_data.get('password1')
				user = authenticate(username=user.username, password=password)
				firstname = form.cleaned_data.get('firstname')
				lastname = form.cleaned_data.get('lastname')
				agentid = form.cleaned_data.get('agent')
				street = form.cleaned_data.get('street')
				city = form.cleaned_data.get('city')
				country = form.cleaned_data.get('country')
				customer = Customer()
				customer.customer_id = user
				customer.agent_id = agentid
				customer.first_name = firstname
				customer.last_name = lastname
				customer.street = street
				customer.city = city
				customer.country = country
				customer.save()

				auth_login(request, user)
				return HttpResponseRedirect(reverse('catalog:index'))
			else:
				return render(request, 'del3/signup.html', {'form': form})
		else:
			form = SignUpForm()
			return render(request, 'del3/signup.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def signup_agent(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = SignUpAgentForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.save()
				password = form.cleaned_data.get('password1')
				user = authenticate(username=user.username, password=password)
				agent = Agent()
				agent.agent_id = user
				agent.total_transaction = 0
				agent.save()

				auth_login(request, user)
				return HttpResponseRedirect(reverse('catalog:index'))
			else:
				return render(request, 'del3/signupagent.html', {'form': form})
		else:
			form = SignUpAgentForm()
			return render(request, 'del3/signupagent.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						auth_login(request, user)
						return HttpResponseRedirect(reverse('index'))
					else:
						return HttpResponse('User inactive')
				else:
					return render(request, 'del3/login.html', {'form': form, 'warning': 'Username or password is incorrect.'})
			else:
				return render(request, 'del3/login.html', {'form': form})
		else:
			form = LoginForm()
			return render(request, 'del3/login.html', {'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse('index'))

def set_passwords(request):
	users = User.objects.all()
	for user in users:
		user.set_password('test')
		user.save()
	return HttpResponseRedirect(reverse('index'))

def cart(request):
	form = CartForm()
	if request.user.is_authenticated():
		try:
			agent = Agent.objects.get(agent_id=request.user.pk)
			return HttpResponseRedirect(reverse('index'))
		except Agent.DoesNotExist:
			if request.method == 'POST' and OrderInfo.objects.filter(customer_id=request.user.id, issue_date=None, cart_ready=False).exists():
				form = CartForm(request.POST)
				if form.is_valid():
					recipient = form.save()
					user_cart = OrderInfo.objects.get(customer_id=request.user.id, issue_date=None, cart_ready=False)
					content_list = Content.objects.filter(order_id=user_cart)
					user_cart.cart_ready = True
					user_cart.save()
					delivery = Delivery(order_id=user_cart, recipient_id=recipient)
					delivery.gift = True
					delivery.save()
					request.session['message'] = "Checkout Successful!"
					return redirect('cart')	
			try:
				user_cart = OrderInfo.objects.get(customer_id=request.user.id, issue_date=None, cart_ready=False)
				content_list = Content.objects.filter(order_id=user_cart)
				request.session['message'] = ""
			except OrderInfo.DoesNotExist:
				user_cart = None
				content_list = None
			content_attribs = Content._meta.fields
			if 'message' in request.session:
				message = request.session['message']
				return render(request, 'del3/cart.html', {'content_attribs': content_attribs, 'content_list': content_list, 'message': message, 'form': form})
			return render(request, 'del3/cart.html', {'content_attribs': content_attribs, 'content_list': content_list, 'form': form})
	else:
		return HttpResponseRedirect(reverse('index'))

def checkout(request):
	if request.user.is_authenticated():
		if request.method == 'POST' and OrderInfo.objects.filter(customer_id=request.user.id, issue_date=None, cart_ready=False).exists():
			pass		
		elif OrderInfo.objects.filter(customer_id=request.user.id, issue_date=None, cart_ready=False).exists():
			#when recipient is self
			customer = Customer.objects.get(customer_id=request.user.id)
			agent = Agent.objects.get(agent_id=customer.agent_id.agent_id)
			user_cart = OrderInfo.objects.get(customer_id=request.user.id, issue_date=None, cart_ready=False)
			content_list = Content.objects.filter(order_id=user_cart)
			user_cart.cart_ready = True
			user_cart.save()
			customer = Customer.objects.get(pk=request.user.id)
			try:
				recipient = Recipient.objects.get(first_name=request.user.first_name)
			except Recipient.DoesNotExist:
				recipient = Recipient()
				recipient.first_name = request.user.first_name
				recipient.last_name = request.user.last_name
				recipient.street = customer.street
				recipient.city = customer.city
				recipient.country = customer.country
				recipient.save()
			delivery = Delivery(delivery_id = user_cart.order_id, order_id=user_cart, recipient_id=recipient)
			delivery.save()
			agent.total_transactions += 1
			agent.save()
			request.session['message'] = "Checkout Successful!"
			return redirect('cart')	
		else:
			request.session['message'] = "No items in cart"
			return redirect('cart')
			
def delete_cart_entry(request, content_id):
	content = Content.objects.get(pk=content_id)
	content.delete()
	return HttpResponseRedirect(reverse('cart'))	