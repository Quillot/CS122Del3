# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_invite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='invite_code',
            field=models.IntegerField(primary_key=True, blank=True, default=11111, serialize=False),
        ),
    ]
