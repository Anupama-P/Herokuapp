# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Site, SiteHoldings

admin.site.register(Site)
admin.site.register(SiteHoldings)
