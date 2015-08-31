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


class Skill(CodeMixin, NameMixin, DescriptionMixin):

    ATTRIBUTE_CHOICES = (
        ('strength', 'Strength'),
        ('constitution', 'Constitution'),
        ('agility', 'Agility'),
        ('intelligence', 'Intelligence'),
        ('mental_strength', 'Mental strength'),
        ('sociability', 'Sociability'),
    )

    TYPE_CHOICES = (
        ('base', 'Base'),
        ('advanced', 'Advanced'),
    )
    attribute = models.CharField(choices=ATTRIBUTE_CHOICES, max_length=30, blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=30, default='base')
    linked_talents = models.ManyToManyField(Talent, blank=True, related_name='linked_skills')
    linked_skill = models.ForeignKey('self', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('skills:index') + '#{0}'.format(self.code)


class SkillSet(models.Model):
    skill0 = models.ForeignKey(Skill, related_name='skillsets_0')
    skill1 = models.ForeignKey(Skill, null=True, blank=True, related_name='skillsets_1')

    class Meta:
        unique_together = ('skill0', 'skill1')

class Career(CodeMixin, NameMixin, DescriptionMixin):

    exits = models.ManyToManyField('self', blank=True, symmetrical=False)
    talents = models.ManyToManyField(TalentSet, blank=True)
    skills = models.ManyToManyField(SkillSet, blank=True)

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
