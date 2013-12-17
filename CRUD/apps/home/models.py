# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Upload(models.Model):
    #name = models.CharField(max_length=255)
    docfile = models.FileField(upload_to='uploads/%Y-%m-%d')

    def __str__(self):
		return self.docfile
