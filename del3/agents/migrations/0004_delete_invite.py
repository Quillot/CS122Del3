# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_auto_20170502_2000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Invite',
        ),
    ]
