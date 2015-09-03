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

class AbstractSet(models.Model):
    max_choices = models.IntegerField(default=1)

    class Meta:
        abstract = True

    def __str__(self):
        return '/'.join([choice.name for choice in self.choices.all()])

class DescriptionMixin(models.Model):
    description = models.TextField(null=True, blank=True)
    class Meta:
        abstract = True


class Character(NameMixin):
    background = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)


class Talent(CodeMixin, NameMixin, DescriptionMixin):
    linked_talent = models.ForeignKey('self', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('talents:index') + '#{0}'.format(self.code)

class TalentSet(AbstractSet):
    choices = models.ManyToManyField(Talent, related_name='talentsets')

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


class SkillSet(AbstractSet):
    choices = models.ManyToManyField(Skill, related_name='skillsets')


class Career(CodeMixin, NameMixin, DescriptionMixin):

    exits = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='access')
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
