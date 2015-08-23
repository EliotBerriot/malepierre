# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20150823_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='career',
            name='magic',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='movement',
            field=models.IntegerField(default=0),
        ),
    ]
