# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_talent'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('talent0', models.ForeignKey(to='characters.Talent', related_name='talentsets_0')),
                ('talent1', models.ForeignKey(null=True, to='characters.Talent', blank=True, related_name='talentsets_1')),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='talents',
            field=models.ManyToManyField(blank=True, to='characters.TalentSet'),
        ),
        migrations.AlterUniqueTogether(
            name='talentset',
            unique_together=set([('talent0', 'talent1')]),
        ),
    ]
