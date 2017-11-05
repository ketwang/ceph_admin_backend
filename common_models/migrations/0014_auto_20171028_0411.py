# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0013_auto_20171028_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='api',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
