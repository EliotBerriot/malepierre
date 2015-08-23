# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20150823_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='code',
            field=models.CharField(unique=True, max_length=255, default='none'),
            preserve_default=False,
        ),
    ]
