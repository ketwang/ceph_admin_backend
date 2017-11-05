# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0023_auto_20171029_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolcapacity',
            name='bytes_used',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='poolcapacity',
            name='kb_used',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='poolcapacity',
            name='max_avail',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
    ]
