# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    total_transactions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent'


class Content(models.Model):
    order = models.ForeignKey('Orderinfo')
    product = models.ForeignKey('Product')
    personalization = models.CharField(max_length=255, blank=True, null=True)
    quantity_ordered = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content'
        unique_together = (('order', 'product'),)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Delivery(models.Model):
    order = models.ForeignKey('Orderinfo')
    recipient = models.ForeignKey('Recipient')

    class Meta:
        managed = False
        db_table = 'delivery'
        unique_together = (('order', 'recipient'),)


class Feature(models.Model):
    product = models.ForeignKey('Product', primary_key=True)
    feature_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature'


class Invite(models.Model):
    invite_id = models.AutoField(primary_key=True)
    invite_code = models.IntegerField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite'


class Orderinfo(models.Model):
    order_id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent)
    customer = models.ForeignKey(Customer)
    recipient = models.ForeignKey('Recipient', blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    issue_time = models.TimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderinfo'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    quantity_stocked = models.IntegerField(blank=True, null=True)
    personalization_limit = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Recipient(models.Model):
    recipient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipient'
