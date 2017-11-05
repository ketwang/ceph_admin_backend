# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0014_auto_20171028_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='osd',
            name='exists',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
