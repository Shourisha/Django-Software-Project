# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Blog(models.Model):
    Title   = models.CharField(max_length=30)
    Body    = models.CharField(max_length=500)

