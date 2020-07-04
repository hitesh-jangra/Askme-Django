# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Blog
from django.db import models

# Register your models here.

admin.site.register(Blog)


