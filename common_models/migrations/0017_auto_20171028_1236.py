# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0016_auto_20171028_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='cluster',
            field=models.ForeignKey(to='common_models.Cluster', null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
