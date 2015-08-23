# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20150823_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
