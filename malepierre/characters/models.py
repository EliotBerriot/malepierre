# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class CodeMixin(models.Model):
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

class NameMixin(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)


class DescriptionMixin(models.Model):
    description = models.TextField(null=True, blank=True)
    class Meta:
        abstract = True


class Character(NameMixin):
    background = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Career(CodeMixin, NameMixin, DescriptionMixin):

    access = models.ManyToManyField('self')
    exits = models.ManyToManyField('self')

    # main profile
    cc = models.IntegerField(default=0)
    ct = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    mental_strength = models.IntegerField(default=0)
    sociability = models.IntegerField(default=0)

    # secondary profile
    attacks = models.IntegerField(default=0)
    wounds = models.IntegerField(default=0)
    movement = models.IntegerField(default=0)
    magic = models.IntegerField(default=0)
