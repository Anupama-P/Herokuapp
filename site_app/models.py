# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from decimal import Decimal


class Site(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class SiteHoldings(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='site_holdings')
    a_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    b_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.site.name
