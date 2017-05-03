# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20170502_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('invite_code', models.IntegerField(primary_key=True, blank=True, default=1, serialize=False)),
                ('used', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'invitation',
            },
        ),
    ]
