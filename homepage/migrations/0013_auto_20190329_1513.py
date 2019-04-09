# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20190329_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='hop_type',
        ),
        migrations.AddField(
            model_name='hoptype',
            name='added_at',
            field=models.IntegerField(blank=True, help_text='ka\xe7inci dakikada eklendi?', null=True),
        ),
        migrations.AddField(
            model_name='hoptype',
            name='hop_quantity',
            field=models.IntegerField(default='1', help_text='gr.'),
        ),
        migrations.AddField(
            model_name='hoptype',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hops', to='homepage.Recipe'),
        ),
    ]