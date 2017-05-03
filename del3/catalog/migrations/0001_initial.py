# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, default='Swiffer')),
                ('color', models.CharField(max_length=255, default='red', choices=[('red', 'red'), ('orange', 'orange'), ('yellow', 'yellow'), ('green', 'green'), ('blue', 'blue'), ('indigo', 'indigo'), ('violet', 'violet'), ('black', 'black'), ('pink', 'pink')])),
                ('quantity_stocked', models.PositiveIntegerField(default=1)),
                ('personalization_limit', models.IntegerField(default=8)),
                ('price', models.FloatField(default=20.0)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('product_id', models.ForeignKey(primary_key=True, default=1, serialize=False, to='catalog.Product')),
                ('feature_desc', models.CharField(max_length=255, default='')),
            ],
            options={
                'db_table': 'feature',
            },
        ),
    ]
