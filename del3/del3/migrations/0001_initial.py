# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('invite_code', models.IntegerField(primary_key=True, blank=True, default=11111, serialize=False)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'invites',
            },
        ),
    ]
