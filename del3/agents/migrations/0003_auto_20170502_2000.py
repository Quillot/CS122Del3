# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20170502_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('invite_code', models.IntegerField(primary_key=True, blank=True, default=11111, serialize=False)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'invitation',
            },
        ),
        migrations.RemoveField(
            model_name='agent',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='last_name',
        ),
    ]
