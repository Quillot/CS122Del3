# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_auto_20170502_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_id',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, db_column='customer_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
