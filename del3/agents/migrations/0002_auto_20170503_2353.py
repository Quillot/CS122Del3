# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_id',
            field=models.OneToOneField(primary_key=True, serialize=False, db_column='agent_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='total_transactions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
