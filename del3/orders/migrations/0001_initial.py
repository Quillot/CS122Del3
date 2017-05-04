# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20170503_2353'),
        ('customers', '__first__'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, unique=True, serialize=False)),
                ('personalization', models.CharField(max_length=255, default='')),
                ('quantity_ordered', models.PositiveIntegerField(default=1)),
                ('discount', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, unique=True, serialize=False)),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.AutoField(primary_key=True, unique=True, serialize=False)),
                ('issue_date', models.DateField(default='2017-01-01')),
                ('issue_time', models.TimeField()),
                ('delivery_date', models.DateField(default='2017-01-01')),
                ('delivery_time', models.TimeField()),
                ('agent_id', models.ForeignKey(default=2, db_column='agent_id', to='agents.Agent')),
                ('customer_id', models.ForeignKey(default=4, db_column='customer_id', to='customers.Customer')),
            ],
            options={
                'db_table': 'orderinfo',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('recipient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, default='Ruscie')),
                ('last_name', models.CharField(max_length=255, default='Pient')),
                ('street', models.CharField(max_length=255, default='Shiny Street')),
                ('city', models.CharField(max_length=255, default='Clean City')),
                ('country', models.CharField(max_length=255, default='Cool Country')),
            ],
            options={
                'db_table': 'recipient',
            },
        ),
        migrations.AddField(
            model_name='delivery',
            name='order_id',
            field=models.OneToOneField(db_column='order_id', to='orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='recipient_id',
            field=models.ForeignKey(default=1, db_column='recipient_id', to='orders.Recipient'),
        ),
        migrations.AddField(
            model_name='content',
            name='order_id',
            field=models.ForeignKey(db_column='order_id', to='orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='content',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', to='catalog.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='delivery',
            unique_together=set([('order_id', 'recipient_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('order_id', 'product_id')]),
        ),
    ]
