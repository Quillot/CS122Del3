# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('agents', '0002_auto_20170503_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.OneToOneField(primary_key=True, serialize=False, db_column='customer_id', to=settings.AUTH_USER_MODEL)),
                ('street', models.CharField(max_length=255, default='Shiny Street')),
                ('city', models.CharField(max_length=255, default='Clean City')),
                ('country', models.CharField(max_length=255, default='Cool Country')),
                ('agent_id', models.ForeignKey(default=2, db_column='agent_id', to='agents.Agent')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
