# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0031_auto_20171104_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbd',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rbd',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='step1',
            field=models.ForeignKey(to='common_models.Crush'),
        ),
        migrations.AlterModelTable(
            name='rbd',
            table='rbd',
        ),
    ]
