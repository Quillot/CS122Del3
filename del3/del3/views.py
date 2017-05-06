from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User

from customers.models import Customer
from agents.models import Agent
from orders.models import OrderInfo, Content

from .forms import SignUpForm, LoginForm, SignUpAgentForm

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
	try:
		user_cart = OrderInfo.objects.get(customer_id=request.user.id, issue_date=None)
		content_list = Content.objects.filter(order_id=user_cart)
	except OrderInfo.DoesNotExist:
		user_cart = None
		content_list = None
	content_attribs = Content._meta.fields
	if request.user.is_authenticated():
		return render(request, 'del3/cart.html', {'user_cart': user_cart, 'content_attribs': content_attribs, 'content_list': content_list})
	else:
		return HttpResponseRedirect(reverse('index'))