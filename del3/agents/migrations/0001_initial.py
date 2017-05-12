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
                ('agent_id', models.OneToOneField(primary_key=True, serialize=False, db_column='agent_id', to=settings.AUTH_USER_MODEL)),
                ('total_transactions', models.PositiveIntegerField(default=0)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
    ]
