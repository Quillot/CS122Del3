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
                ('invite_id', models.AutoField(primary_key=True, serialize=False)),
                ('invite_code', models.IntegerField(default=11111)),
                ('used', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'invite',
            },
        ),
    ]
