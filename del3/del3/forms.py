from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from customers.models import Customer
from agents.models import Agent
from .models import Invite
from orders.models import Recipient


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30, required=True, help_text='Required')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required')
	email = forms.EmailField(max_length=254, required=True, help_text = 'Required')
	agent = forms.ModelChoiceField(queryset=Agent.objects.all(), required=True, help_text='Choose an agent to handle your orders')
	street = forms.CharField(max_length=255, required=True, help_text = 'Required')
	city = forms.CharField(max_length=255, required=True, help_text = 'Required')
	country = forms.CharField(max_length=255, required=True, help_text = 'Required')


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 
			'password2', 'email', 'agent', 'street', 'city', 'country')

	def save(self, commit=False):
		user = User.objects.create_user(username=self.clean_username(), password=self.cleaned_data['password1'])
		user.email = self.clean_email()
		user.first_name = self.cleaned_data.get('first_name').title()
		user.last_name = self.cleaned_data.get('last_name').title()
		fields = user._meta.fields
		for field in fields:
			if field is not None:
				all_clear = True
			else:
				all_clear = False
		if fields[-1] is not None and all_clear and commit:
			user.save()
		return user

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username already in use')
		else:
			return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email already in use')
		else:
			return email

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30, required=True)
	password = forms.CharField(widget=forms.PasswordInput(), max_length=30, required=True)

class SignUpAgentForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30, required=True, help_text='Required')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required')
	email = forms.EmailField(max_length=254, required=True, help_text='Required')
	code = forms.IntegerField(required=True, help_text='Enter invitation code')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 
			'password2', 'email', 'code')

	def save(self, commit=False):
		user = User.objects.create_user(username=self.clean_username(), password=self.cleaned_data['password1'])
		user.email = self.clean_email()
		user.first_name = self.cleaned_data.get('first_name').title()
		user.last_name = self.cleaned_data.get('last_name').title()
		code = self.clean_code()[0]
		if code:
			code.used = True
			code.save()
		fields = user._meta.fields
		for field in fields:
			if field is not None:
				all_clear = True
			else:
				all_clear = False
		if fields[-1] is not None and all_clear and commit:
			user.save()
		return user

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username already in use')
		else:
			return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email already in use')
		else:
			return email

	def clean_code(self):
		invite_code = self.cleaned_data.get('code')
		code = Invite.objects.filter(invite_code=invite_code)
		if len(code) == 0:
			raise forms.ValidationError('Code not found')
		elif code[0].used == 1:
			raise forms.ValidationError('Code already used')
		else:
			return code

class CartForm(forms.Form):
	first_name = forms.CharField(max_length=255, required=True)
	last_name = forms.CharField(max_length=255, required=True)
	street = forms.CharField(max_length=255, required=True)
	city = forms.CharField(max_length=255, required=True)
	country = forms.CharField(max_length=255, required=True)

	def save(self, commit=False):
		recipient = Recipient()
		first_name = self.cleaned_data.get('first_name')
		last_name = self.cleaned_data.get('last_name')
		street = self.cleaned_data.get('street')
		city = self.cleaned_data.get('city')
		country = self.cleaned_data.get('country')
		recipient.first_name = first_name
		recipient.last_name = last_name
		recipient.street = street
		recipient.city = city
		recipient.country = country
		fields = recipient._meta.fields

		for field in fields:
			if field is not None:
				all_clear = True
			else:
				all_clear = False
		if fields[-1] is not None and all_clear:
			recipient.save()
		return recipient