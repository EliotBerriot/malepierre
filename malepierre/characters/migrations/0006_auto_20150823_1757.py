# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20150823_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='access',
        ),
        migrations.AlterField(
            model_name='career',
            name='exits',
            field=models.ManyToManyField(blank=True, to='characters.Career'),
        ),
    ]
