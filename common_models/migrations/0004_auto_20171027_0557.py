# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_models', '0003_auto_20171027_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crush',
            name='children',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
