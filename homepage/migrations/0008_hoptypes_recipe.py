# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-28 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20190328_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoptypes',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hop_type', to='homepage.Recipes'),
        ),
    ]
