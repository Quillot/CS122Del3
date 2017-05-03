# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '__first__'),
        ('agents', '0004_delete_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('personalization', models.CharField(max_length=255, blank=True, null=True)),
                ('quantity_ordered', models.IntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.AutoField(primary_key=True, unique=True, serialize=False)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('issue_time', models.TimeField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('delivery_time', models.TimeField(blank=True, null=True)),
                ('agent_id', models.ForeignKey(default=1, db_column='agent_id', to='agents.Agent')),
            ],
            options={
                'db_table': 'orderinfo',
            },
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('recipient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, blank=True, null=True)),
                ('last_name', models.CharField(max_length=255, blank=True, null=True)),
                ('street', models.CharField(max_length=255, blank=True, null=True)),
                ('city', models.CharField(max_length=255, blank=True, null=True)),
                ('country', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'db_table': 'recipient',
            },
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='recipient_id',
            field=models.ForeignKey(default=1, db_column='recipient_id', to='orders.Recipient'),
        ),
        migrations.AddField(
            model_name='content',
            name='order_id',
            field=models.ForeignKey(default=1, db_column='order_id', to='orders.OrderInfo'),
        ),
        migrations.AddField(
            model_name='content',
            name='product_id',
            field=models.ForeignKey(default=1, db_column='product_id', to='catalog.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([('order_id', 'product_id')]),
        ),
    ]
