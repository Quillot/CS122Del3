# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20170502_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='used',
            field=models.BooleanField(default=0),
        ),
    ]
