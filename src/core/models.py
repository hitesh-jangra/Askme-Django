# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

#Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=400)
    category=models.CharField(max_length=200)
    content=RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('visitblog',kwargs={"id":self.id})

    class Meta:
        ordering = ['-title']