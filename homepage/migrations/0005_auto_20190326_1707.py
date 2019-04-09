# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190326_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='abv',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='final_gravity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='original_gravity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=4, null=True),
        ),
    ]
