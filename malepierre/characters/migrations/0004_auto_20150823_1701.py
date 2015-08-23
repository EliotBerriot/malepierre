# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_career_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='agility',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='attacks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='cc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='constitution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='ct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='intelligence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='mental_strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='sociability',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='wounds',
            field=models.IntegerField(default=0),
        ),
    ]
