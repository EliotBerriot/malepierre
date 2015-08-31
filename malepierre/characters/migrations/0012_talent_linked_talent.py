# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20150831_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='linked_talent',
            field=models.ForeignKey(blank=True, to='characters.Talent', null=True),
        ),
    ]
