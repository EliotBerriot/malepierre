# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20150823_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(unique=True, max_length=255)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('attribute', models.CharField(choices=[('strength', 'Strength'), ('constitution', 'Constitution'), ('agility', 'Agility'), ('intelligence', 'Intelligence'), ('mental_strength', 'Mental strength'), ('sociability', 'Sociability')], blank=True, max_length=30, null=True)),
                ('type', models.CharField(choices=[('base', 'Base'), ('advanced', 'Advanced')], max_length=30, default='base')),
                ('linked_skill', models.ForeignKey(to='characters.Skill', null=True, blank=True)),
                ('linked_talents', models.ManyToManyField(to='characters.Talent', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
