# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20150823_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillset',
            name='choices',
            field=models.ManyToManyField(related_name='skillsets', to='characters.Skill'),
        ),
        migrations.AddField(
            model_name='skillset',
            name='max_choices',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='talentset',
            name='choices',
            field=models.ManyToManyField(related_name='talentsets', to='characters.Talent'),
        ),
        migrations.AddField(
            model_name='talentset',
            name='max_choices',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='skillset',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='talentset',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='skillset',
            name='skill0',
        ),
        migrations.RemoveField(
            model_name='skillset',
            name='skill1',
        ),
        migrations.RemoveField(
            model_name='talentset',
            name='talent0',
        ),
        migrations.RemoveField(
            model_name='talentset',
            name='talent1',
        ),
    ]
