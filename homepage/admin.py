# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from homepage.models import Recipe, HopType

# Register your models here.

admin.site.register(Recipe)
admin.site.register(HopType)
