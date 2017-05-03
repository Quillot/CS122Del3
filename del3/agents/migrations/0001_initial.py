# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('agent_id', models.OneToOneField(primary_key=True, default=1, serialize=False, db_column='user_id', to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255, blank=True, null=True)),
                ('last_name', models.CharField(max_length=255, blank=True, null=True)),
                ('total_transactions', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
    ]
