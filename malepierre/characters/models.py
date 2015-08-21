# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Character(models.Model):
    name = models.CharField(max_length=255)
    background = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
