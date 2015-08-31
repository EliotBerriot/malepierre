# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='linked_talents',
            field=models.ManyToManyField(blank=True, related_name='linked_skills', to='characters.Talent'),
        ),
        migrations.AddField(
            model_name='skillset',
            name='skill0',
            field=models.ForeignKey(related_name='skillsets_0', to='characters.Skill'),
        ),
        migrations.AddField(
            model_name='skillset',
            name='skill1',
            field=models.ForeignKey(blank=True, related_name='skillsets_1', to='characters.Skill', null=True),
        ),
        migrations.AddField(
            model_name='career',
            name='skills',
            field=models.ManyToManyField(blank=True, to='characters.SkillSet'),
        ),
        migrations.AlterUniqueTogether(
            name='skillset',
            unique_together=set([('skill0', 'skill1')]),
        ),
    ]
