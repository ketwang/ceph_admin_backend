# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0007_rule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='rule_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
