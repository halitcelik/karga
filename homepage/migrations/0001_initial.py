# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('style', models.CharField(max_length=112)),
                ('difficulty', models.CharField(choices=[(('easy',), 'Easy'), (('medium',), 'Medium'), ('difficult', 'Difficult')], max_length=10)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('ingredients', models.CharField(max_length=1024)),
                ('image', models.ImageField(upload_to='images/')),
                ('long_description', models.CharField(max_length=1024)),
            ],
        ),
    ]
