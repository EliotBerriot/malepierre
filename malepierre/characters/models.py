# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class CodeMixin(models.Model):
    code = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True

class NameMixin(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name

class DescriptionMixin(models.Model):
    description = models.TextField(null=True, blank=True)
    class Meta:
        abstract = True


class Character(NameMixin):
    background = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

class Talent(CodeMixin, NameMixin, DescriptionMixin):

    def get_absolute_url(self):
        return reverse('talents:index') + '#{0}'.format(self.code)

class TalentSet(models.Model):
    talent0 = models.ForeignKey(Talent, related_name='talentsets_0')
    talent1 = models.ForeignKey(Talent, null=True, blank=True, related_name='talentsets_1')

    class Meta:
        unique_together = ('talent0', 'talent1')

class Career(CodeMixin, NameMixin, DescriptionMixin):

    exits = models.ManyToManyField('self', blank=True, symmetrical=False)
    talents = models.ManyToManyField(TalentSet, blank=True)

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

    def get_absolute_url(self):
        return reverse('careers:index') + '#{0}'.format(self.code)
