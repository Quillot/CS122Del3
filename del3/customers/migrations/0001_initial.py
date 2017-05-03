# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('agents', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.OneToOneField(primary_key=True, blank=True, default=1, serialize=False, db_column='customer_id', to=settings.AUTH_USER_MODEL)),
                ('street', models.CharField(max_length=255, blank=True, null=True)),
                ('city', models.CharField(max_length=255, blank=True, null=True)),
                ('country', models.CharField(max_length=255, blank=True, null=True)),
                ('agent_id', models.ForeignKey(blank=True, null=True, default=1, db_column='agent_id', to='agents.Agent')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
