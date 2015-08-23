# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('access', models.ManyToManyField(to='characters.Career', related_name='access_rel_+')),
                ('exits', models.ManyToManyField(to='characters.Career', related_name='exits_rel_+')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
