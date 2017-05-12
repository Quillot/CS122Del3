# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('feature_desc', models.CharField(max_length=255, default='')),
            ],
            options={
                'db_table': 'feature',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, default='Swiffer')),
                ('color', models.CharField(max_length=255, default='red', choices=[('red', 'red'), ('orange', 'orange'), ('yellow', 'yellow'), ('green', 'green'), ('blue', 'blue'), ('purple', 'purple'), ('black', 'black'), ('pink', 'pink')])),
                ('quantity_stocked', models.PositiveIntegerField(default=1)),
                ('personalization_limit', models.IntegerField(default=8)),
                ('price', models.FloatField(default=20.0)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.AddField(
            model_name='feature',
            name='product_id',
            field=models.ForeignKey(default=1, db_column='product_id', to='catalog.Product'),
        ),
    ]
