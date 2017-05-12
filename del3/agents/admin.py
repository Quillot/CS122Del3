from django.contrib import admin
from agents.models import Agent
from catalog.models import Product, Feature
from customers.models import Customer
from del3.models import Invite
from orders.models import OrderInfo, Content, Delivery

admin.site.register(Agent)
admin.site.register(Product)
admin.site.register(Feature)
admin.site.register(Customer)
admin.site.register(Invite)
admin.site.register(OrderInfo)
admin.site.register(Content)
admin.site.register(Delivery)