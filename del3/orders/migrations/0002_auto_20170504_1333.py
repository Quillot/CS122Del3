# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='delivery_time',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='issue_time',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='delivery',
            unique_together=set([]),
        ),
    ]
