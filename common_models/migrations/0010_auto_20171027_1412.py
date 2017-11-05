# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0009_auto_20171027_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='osdproperty',
            name='cluster',
            field=models.ForeignKey(to='common_models.Cluster', null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
